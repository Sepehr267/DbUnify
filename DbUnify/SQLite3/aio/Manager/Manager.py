from typing import List, Tuple, Dict, Union, Optional, Any
import aiosqlite
import logging
from ...data.Rules import Rules
from ..Cache import Cache
from ....SQL.SQLInjection import SQLInjection

logging.basicConfig(filename='sql_errors.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

class Manager:
    """
    Manager Class:
    
    The Manager class provides an interface for managing SQLite databases asynchronously. It offers methods for connecting to the database, executing SQL queries, creating and modifying tables, inserting and deleting rows, and closing the database connection.
    
    Attributes:
        db_name (str): The name of the SQLite database.
        raw (Raw): An instance of the Raw class for executing raw SQL queries.
        connection: The connection object to the SQLite database.
        cursor: The cursor object for executing SQL queries.
        cache (Cache): An instance of the Cache class for caching query results.
        sql_injection_detection (bool): Enable or disable SQL injection detection.
        sql_injection_detector (SQLInjection): Instance of SQLInjection class for detecting SQL injection.
    
    Methods:
        __init__(self, db_name): Initializes the Manager instance with the name of the SQLite database.
        connect(self): Asynchronously connects to the SQLite database.
        fetch_all(self, query, *args): Executes a query and fetches all results asynchronously.
        create_table(self, table_name, columns): Creates a table in the database asynchronously.
        drop_table(self, table_name): Drops a table from the database asynchronously.
        add_column(self, table_name, column_name, data_type, constraints): Adds a column to an existing table asynchronously.
        insert_row(self, table_name, values): Inserts a row into the table asynchronously.
        delete_column(self, table_name, column_name): Deletes a column from the table asynchronously.
        delete_row(self, table_name, condition): Deletes a row from the table based on a condition asynchronously.
        update_row(self, table_name, values, condition): Updates a row in the table based on a condition asynchronously.
        select_one(self, table_name, condition): Searches for a single row in the table based on a condition asynchronously.
        select(self, table_name): Searches for all rows in the table asynchronously.
        get_table_columns(self, table_name): Gets columns and their data types for a table asynchronously.
        close(self): Closes the database connection asynchronously.
    
    Raises:
        ConnectionError: If there is an error connecting to or closing the database.
        RuntimeError: If there is an error executing SQL queries, creating or modifying tables, inserting or deleting rows, or searching for rows.
    
    Note:
        The 'Raw' class is used internally for executing raw SQL queries.
    """
    
    def __init__(self, db_name: str, cache_ttl: int = 300, sql_injection_detection: bool = False) -> None:
        """
        Initialize the Manager instance.

        Args:
            db_name (str): The name of the SQLite database.
            cache_ttl (int): Time-to-live for cache entries in seconds. Default is 300 seconds (5 minutes).
            sql_injection_detection (bool): Enable or disable SQL injection detection. Default is False.
        """
        from ..Raw.Raw import Raw
        self.db_name = db_name
        self.cache = Cache(ttl=cache_ttl)
        self.connection = None
        self.cursor = None
        self.raw = Raw(self)
        self.sql_injection_detection = sql_injection_detection
        self.sql_injection_detector = SQLInjection()
    
    async def __aenter__(self):
        self.connection = await aiosqlite.connect(self.db_name)
        self.cursor = await self.connection.cursor()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            await self.connection.close()

    async def connect(self) -> None:
        """
        Connect to the SQLite database asynchronously.
        """
        try:
            self.connection = await aiosqlite.connect(self.db_name)
            self.cursor = await self.connection.cursor()
        except aiosqlite.Error as e:
            raise ConnectionError(f"Error connecting to the database: {str(e)}")

    def _check_for_injection(self, query: str, *args) -> bool:
        """
        Checks the query for potential SQL injection patterns if detection is enabled.

        Args:
            query (str): The SQL query to check.

        Returns:
            bool: True if potential SQL injection is detected, False otherwise.
        """
        if self.sql_injection_detection:
            check = self.sql_injection_detector.detect(query, *args)
            if check:
                logging.error(f"Potential SQL injection detected. SQL Command: {query}, Parameters: {args}")
                return True
        return False
        
    async def fetch_all(self, query: str, *args) -> List[Tuple]:
        """
        Execute a query and fetch all results asynchronously.

        Args:
            query (str): The SQL query to be executed.
            *args: Parameters to be passed to the query.

        Returns:
            list: List of fetched rows.

        Raises:
            RuntimeError: If there is an error fetching data.
        """
        if self._check_for_injection(query, *args):
            return []
        try:
            await self.cursor.execute(query, args)
            return await self.cursor.fetchall()
        except aiosqlite.Error as e:
            logging.error(f"Error executing query: {str(e)}")
            raise RuntimeError(f"Error executing query: {str(e)}")

    async def create_table(self, table_name: str, columns: List[Tuple[str, str, Optional[List[Union[str, Rules]]]]]) -> None:
        """
        Create a table in the database asynchronously.
        
        Args:
            table_name (str): Name of the table to be created.
            columns (list): List of tuples containing column names, data types, and rules.

        Raises:
            RuntimeError: If there is an error creating the table.
        """
        if self.connection is None:
            raise RuntimeError("Database connection is not initialized.")
        try:
            columns_definitions = []
            for col_name, data_type, rules in columns:
                rules_str = ' '.join(rule.value for rule in rules) if rules else ''
                columns_definitions.append(f"{col_name} {data_type} {rules_str}")
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns_definitions)})"
            if self._check_for_injection(query):
                return
            await self.raw.execute_query(query)
        except aiosqlite.Error as e:
            logging.error(f"Error creating table: {str(e)}")
            raise RuntimeError(f"Error creating table: {str(e)}")

    async def drop_table(self, table_name: str) -> None:
        """
        Drop a table from the database asynchronously.
        
        Args:
            table_name (str): Name of the table to be dropped.

        Raises:
            RuntimeError: If there is an error dropping the table.
        """
        query = f"DROP TABLE IF EXISTS {table_name}"
        if self._check_for_injection(query):
            return
        try:
            await self.raw.execute_query(query)
        except aiosqlite.Error as e:
            logging.error(f"Error dropping table: {str(e)}")
            raise RuntimeError(f"Error dropping table: {str(e)}")

    async def add_column(self, table_name: str, column_name: str, data_type: str,) -> None:
        """
        Add a column to an existing table asynchronously.
        
        Args:
            table_name (str): Name of the table to add the column to.
            column_name (str): Name of the column to be added.
            data_type (str): Data type of the column.

        Raises:
            RuntimeError: If there is an error adding the column.
        """
        query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type}"
        if self._check_for_injection(query):
            return
        try:
            await self.raw.execute_query(query)
        except aiosqlite.Error as e:
            logging.error(f"Error adding column: {str(e)}")
            raise RuntimeError(f"Error adding column: {str(e)}")

    async def insert_row(self, table_name: str, values: Dict[str, Union[str, int, float]]) -> None:
        """
        Insert a row into the table asynchronously.
        
        Args:
            table_name (str): Name of the table to insert the row into.
            values (dict): Dictionary of column names and values to be inserted.

        Raises:
            RuntimeError: If there is an error inserting the row.
        """
        columns = ', '.join(values.keys())
        placeholders = ', '.join(['?'] * len(values))
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        if self._check_for_injection(query, *values.values()):
            return
    
        try:
            values_tuple = tuple(values.values())

            await self.raw.execute_query(query, *values_tuple)
        except aiosqlite.Error as e:
            logging.error(f"Error inserting row: {str(e)}")
            raise RuntimeError(f"Error inserting row: {str(e)}")

    async def delete_column(self, table_name: str, column_name: str) -> None:
        """
        Delete a column from the table after taking a backup of the table asynchronously.

        Args:
            table_name (str): Name of the table.
            column_name (str): Name of the column to be deleted.

        Raises:
            RuntimeError: If there is an error deleting the column.
        """
        try:
            backup_table_name = f"{table_name}_backup"
            temp_table_name = f"{table_name}_temp"
            
            await self._backup_table(table_name, backup_table_name)
            
            current_columns = await self._get_table_columns_delete_column(table_name)
            columns_to_keep = [col for col in current_columns if col != column_name]

            columns_definitions = ', '.join([f"{col} {current_columns[col]}" for col in columns_to_keep])
            await self.raw.execute_query(f"CREATE TABLE {temp_table_name} ({columns_definitions})")

            columns_names = ', '.join(columns_to_keep)
            await self.raw.execute_query(f"INSERT INTO {temp_table_name} SELECT {columns_names} FROM {table_name}")

            await self.drop_table(table_name)
            await self.drop_table(backup_table_name)

            await self.raw.execute_query(f"ALTER TABLE {temp_table_name} RENAME TO {table_name}")

        except aiosqlite.Error as e:
            logging.error(f"Error deleting column: {str(e)}")
            raise RuntimeError(f"Error deleting column: {str(e)}")

    async def delete_row(self, table_name: str, condition_column: str, condition_value: str) -> None:

        """
        Delete a row from the table based on a condition asynchronously.
        
        Args:
            table_name (str): Name of the table to delete the row from.
            condition_column (str): Column name for the condition.
            condition_value (str): Value for the condition.

        Raises:
            RuntimeError: If there is an error deleting the row.
        """
        query = f"DELETE FROM {table_name} WHERE {condition_column} = ?"
        if self._check_for_injection(query):
            return
        try:
            await self.raw.execute_query(query, condition_value)
        except aiosqlite.Error as e:
            logging.error(f"Error deleting row: {str(e)}")
            raise RuntimeError(f"Error deleting row: {str(e)}")

    async def update_row(self, table_name: str, values: Dict[str, Union[str, int, float]], condition_column: str, condition_value: str) -> None:
        """
        Update a row in the table based on a condition asynchronously.
        
        Args:
            table_name (str): Name of the table to update the row in.
            values (dict): Dictionary of column names and values to be updated.
            condition_column (str): Column name for the condition.
            condition_value (str): Value for the condition.

        Raises:
            RuntimeError: If there is an error updating the row.
        """
        set_clause = ', '.join([f"{col} = ?" for col in values.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition_column} = ?"

        values_tuple = tuple(values.values()) + (condition_value,) 

        if self._check_for_injection(query, *values.values(), condition_value):
            return
        try:
            await self.raw.execute_query(query, *values_tuple)
        except aiosqlite.Error as e:
            logging.error(f"Error updating row: {str(e)}")
            raise RuntimeError(f"Error updating row: {str(e)}")

    async def select_one(self, table_name: str, **conditions: Dict[str, Any]) -> Optional[Tuple]:
        """
        Search for a single row in the table based on a condition asynchronously.

        Args:
            table_name (str): Name of the table to search in.
            **conditions (dict): Column names and values for the condition.

        Returns:
            tuple: The fetched row.

        Raises:
            RuntimeError: If there is an error searching for the row.
        """
        condition_str = ' AND '.join([f"{col} = ?" for col in conditions.keys()])
        query = f"SELECT * FROM {table_name} WHERE {condition_str}"

        if self._check_for_injection(query, *conditions.values()):
            return None

        try:
            async with self.connection.cursor() as cursor:
                await cursor.execute(query, tuple(conditions.values()))
                row = await cursor.fetchone()
                return row
        except aiosqlite.Error as e:
            logging.error(f"Error selecting row: {str(e)}")
            raise RuntimeError(f"Error selecting row: {str(e)}")
        
    async def select(self, table_name: str) -> List[Tuple]:
        """
        Search for all rows in the table asynchronously.
        
        Args:
            table_name (str): Name of the table to search in.

        Returns:
            list: List of fetched rows.

        Raises:
            RuntimeError: If there is an error searching for rows.
        """
        query = f"SELECT * FROM {table_name}"
        if self._check_for_injection(query):
            return []
        try:
            await self.cursor.execute(query)
            return await self.cursor.fetchall()
        except aiosqlite.Error as e:
            logging.error(f"Error selecting rows: {str(e)}")
            raise RuntimeError(f"Error selecting rows: {str(e)}")

    async def get_table_columns(self, table_name: str) -> List[str]:
        """
        Get columns and their data types for a table asynchronously.
        
        Args:
            table_name (str): Name of the table to get columns for.

        Returns:
            list: List of columns and their data types.

        Raises:
            RuntimeError: If there is an error retrieving columns.
        """
        query = f"PRAGMA table_info({table_name})"
        if self._check_for_injection(query):
            return []
        try:
            await self.cursor.execute(query)
            columns = await self.cursor.fetchall()
            return [col[1] for col in columns] 
        except aiosqlite.Error as e:
            logging.error(f"Error getting table columns: {str(e)}")
            raise RuntimeError(f"Error getting table columns: {str(e)}")

    async def _get_table_columns_delete_column(self, table_name: str) -> Dict[str, str]:
        """
        Get the columns and their data types for a table asynchronously.

        Args:
            table_name (str): Name of the table.

        Returns:
            dict: Dictionary of column names and their data types.

        Raises:
            RuntimeError: If there is an error getting the columns.
        """
        try:
            async with self.connection.execute(f"PRAGMA table_info({table_name})") as cursor:
                columns = await cursor.fetchall()
                return {col[1]: col[2] for col in columns}
        except aiosqlite.Error as e:
            raise RuntimeError(f"Error getting table columns: {str(e)}")
        
    async def _backup_table(self, table_name: str, backup_table_name: str) -> None:
        """
        Create a backup of the specified table asynchronously.

        Args:
            table_name (str): The name of the table to backup.
            backup_table_name (str): The name of the backup table.

        Raises:
            RuntimeError: If there is an error during the backup process.
        """
        try:
            await self.raw.execute_query(f"CREATE TABLE {backup_table_name} AS SELECT * FROM {table_name}")
        except aiosqlite.Error as e:
            logging.error(f"Error creating backup table: {str(e)}")
            raise RuntimeError(f"Error creating backup table: {str(e)}")
        
    async def close(self) -> None:
        """
        Close the database connection asynchronously.
        """
        if self.connection:
            await self.connection.close()
