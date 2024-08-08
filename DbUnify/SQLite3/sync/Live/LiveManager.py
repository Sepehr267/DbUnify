from .LiveException import *
from .obj import Attribute
from typing import Callable, Dict, List
import sqlite3
import time
import json
import threading

class LiveManager:
    def __init__(self, db_name: str, event_ttl: float, cache_ttl: int = 300):
        """
        Initialize the LiveManager with the database name, event checking interval, and cache TTL.

        Args:
            db_name (str): The name of the SQLite database file.
            event_ttl (float): The time interval (in seconds) for checking database changes.
            cache_ttl (int): Time-to-live for cache entries in seconds. Default is 300 seconds (5 minutes).
        """
        self.db_name = db_name
        self.event_ttl = event_ttl
        self.cache_ttl = cache_ttl
        self.callbacks = {}
        self.connection = self._create_connection()
        self.cursor = self.connection.cursor()
        self.tables = self._get_tables()
        self.last_row_ids = self._initialize_last_row_ids()
        self.previous_data = self._get_initial_data()
        self.log_file = 'changes_log.json'
        self._running = False
        self._thread = None
        self.table_schemas = {}

    def _create_connection(self):
        """
        Create a database connection to the SQLite database specified by the db_name.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            raise DatabaseAccessException(f"Error connecting to database: {str(e)}")

    def _execute_query(self, query: str):
        """
        Execute a SQL query and return the result.

        Args:
            query (str): The SQL query to execute.
        """
        try:
            self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            raise DatabaseAccessException(f"Failed to execute query '{query}': {str(e)}")

    def _get_tables(self) -> List[str]:
        """
        Get a list of all tables in the database.

        Returns:
            List[str]: A list of table names.
        """
        query = "SELECT name FROM sqlite_master WHERE type='table'"
        tables = self._execute_query(query)
        return [table[0] for table in tables]

    def _initialize_last_row_ids(self) -> Dict[str, int]:
        """
        Initialize the last row IDs for all tables.

        Returns:
            Dict[str, int]: A dictionary mapping table names to their last row IDs.
        """
        last_row_ids = {}
        for table in self.tables:
            query = f"SELECT MAX(rowid) FROM {table}"
            row_id = self._execute_query(query)[0][0]
            last_row_ids[table] = row_id if row_id else 0
        return last_row_ids

    def _get_initial_data(self) -> Dict[str, Dict[int, tuple]]:
        """
        Get the initial data of all tables.

        Returns:
            Dict[str, Dict[int, tuple]]: A dictionary mapping table names to another dictionary
                                         that maps row IDs to row data.
        """
        initial_data = {}
        for table in self.tables:
            query = f"SELECT rowid, * FROM {table}"
            rows = self._execute_query(query)
            initial_data[table] = {row[0]: row[1:] for row in rows}
        return initial_data

    def _log_change(self, change: Attribute):
        """
        Log changes to a JSON file.

        Args:
            change (Attribute): The change to log.
        """
        try:
            with open(self.log_file, 'a') as f:
                json.dump(change.to_dict(), f)
                f.write('\n')
        except Exception as e:
            raise LogWriteException(f"Failed to write to log file: {str(e)}")

    def register_callback(self, event: str, callback: Callable):
        """
        Register a callback for a specific event.

        Args:
            event (str): The event to register the callback for.
            callback (Callable): The callback function to register.
        """
        if event not in self.callbacks:
            self.callbacks[event] = []
        self.callbacks[event].append(callback)

    def _get_table_schema(self, table: str) -> str:
        """
        Get the schema of a table.

        Args:
            table (str): The name of the table.

        Returns:
            str: The schema of the table.
        """
        query = f"PRAGMA table_info({table})"
        schema = self._execute_query(query)
        return str(schema)

    def _detect_changes(self):
        """
        Detect and log changes to tables and structures.
        """
        for table in self.tables:
            query = f"SELECT rowid, * FROM {table}"
            current_rows = self._execute_query(query)
            current_data = {row[0]: row[1:] for row in current_rows}

            for row_id, row_data in current_data.items():
                if row_id > self.last_row_ids[table]:
                    operation = 'INSERT'
                elif self.previous_data[table].get(row_id) != row_data:
                    operation = 'UPDATE'
                else:
                    continue

                change = Attribute(
                    timestamp=time.strftime('%Y-%m-%d %H:%M:%S'),
                    db_name=self.db_name,
                    table_name=table,
                    operation=operation,
                    command=f"SELECT * FROM {table} WHERE rowid = {row_id}",
                    details=row_data
                )
                self._log_change(change)
                self._trigger_event('change_detected', change)
                self.last_row_ids[table] = max(self.last_row_ids[table], row_id)

            deleted_row_ids = set(self.previous_data[table].keys()) - set(current_data.keys())
            for row_id in deleted_row_ids:
                change = Attribute(
                    timestamp=time.strftime('%Y-%m-%d %H:%M:%S'),
                    db_name=self.db_name,
                    table_name=table,
                    operation='DELETE',
                    command=f"DELETE FROM {table} WHERE rowid = {row_id}",
                    details=self.previous_data[table][row_id]
                )
                self._log_change(change)
                self._trigger_event('change_detected', change)

            self.previous_data[table] = current_data

    def _detect_schema_changes(self):
        """
        Detect and log schema changes.
        """
        for table in self.tables:
            new_schema = self._get_table_schema(table)
            if table in self.table_schemas:
                old_schema = self.table_schemas[table]
                if old_schema != new_schema:
                    change = Attribute(
                        timestamp=time.strftime('%Y-%m-%d %H:%M:%S'),
                        db_name=self.db_name,
                        table_name=table,
                        operation='SCHEMA_CHANGE',
                        command=f"PRAGMA table_info({table})",
                        details={'old_schema': old_schema, 'new_schema': new_schema}
                    )
                    self._log_change(change)
                    self._trigger_event('schema_change_detected', change)
            self.table_schemas[table] = new_schema

    def _trigger_event(self, event: str, change: Attribute):
        """
        Trigger the registered callbacks for a specific event.

        Args:
            event (str): The event to trigger.
            change (Attribute): The change that occurred.
        """
        if event in self.callbacks:
            for callback in self.callbacks[event]:
                try:
                    callback(self, change)
                except Exception as e:
                    raise EventHandlingException(f"Error in event handler for event {event}: {str(e)}")

    def _monitor(self):
        """
        Monitor database changes and schema changes in a separate thread.
        """
        while self._running:
            try:
                self._detect_changes()
                self._detect_schema_changes()
            except Exception as e:
                print(f"Monitoring error: {e}")
            time.sleep(self.event_ttl)

    def start(self):
        """
        Start monitoring the database.
        """
        if not self._running:
            self._running = True
            self._thread = threading.Thread(target=self._monitor, daemon=True)
            self._thread.start()

    def stop(self):
        """
        Stop monitoring the database.
        """
        if self._running:
            self._running = False
            if self._thread:
                self._thread.join()

    def restart(self):
        """
        Restart monitoring the database.
        """
        self.stop()
        self.start()

    def run(self):
        """
        Continuously monitor the database for changes.
        """
        while True:
            try:
                self._detect_changes()
                self._detect_schema_changes()
            except Exception as e:
                print(f"Run error: {e}")
            time.sleep(self.event_ttl)
