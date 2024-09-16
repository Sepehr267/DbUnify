from ..Live.LiveEvents import *
from typing import Any, Dict, List
import base64, binascii

class Raw:
    """
    # Raw Class

    #### The Raw class provides methods for executing raw SQL queries, creating database backups, restoring backups,
    #### listing tables, inserting and reading base64 encoded data.

    ### Attributes:
        - manager (Manager): The Manager instance managing the database connection.

    ### Methods:
        - __init__(self, manager): Initializes the Raw instance with a Manager instance.
        - backup_database(self, backup_path): Creates a backup of the database.
        - restore_database(self, backup_path): Restores the database from a backup.
        - execute_query(self, query, *args): Executes a database query.
        - list_tables(self): Gets a list of all tables in the SQLite database.
        - insert_base64(self, table_name, data_dict): Inserts base64 encoded data into a database table.
        - read_base64(self, table_name, only_base64): Reads and decodes base64 encoded data from a database table.

    ### Raises:
        - RuntimeError: If there is an error during database backup, restoration, query execution, listing tables,
          or reading and decoding base64 data.

    ### Note:
        - This class is designed for asynchronous usage and requires the use of the 'async' and 'await' keywords for method calls.
        - The 'Manager' class is used internally for managing the database connection.
    """
    
    def __init__(self, manager):
        """
        Initialize the Raw Class instance.

        Args:
            manager (Manager): The Manager instance managing the database connection.
        """
        self.manager = manager

    def backup_database(self, backup_path: str) -> bool:
        """
        Create a backup of the database.

        Args:
            backup_path (str): The path where the backup should be stored.

        Returns:
            bool: True if the backup was successful, False otherwise.

        Raises:
            RuntimeError: If there is an error creating the database backup.
        """
        
        try:
            import shutil
            shutil.copyfile(self.manager.db_name, backup_path)
            return True
        except Exception as e:
                raise RuntimeError(f"Error creating database backup: {str(e)}")
        
    def restore_database(self, backup_path: str) -> bool:
        """
        Restore the database from a backup.

        Args:
            backup_path (str): The path to the backup file.

        Returns:
            bool: True if the restore was successful, False otherwise.

        Raises:
            RuntimeError: If there is an error restoring the database.
        """
        try:
            import shutil
            shutil.copyfile(backup_path, self.manager.db_name)
            return True
        except Exception as e:
            raise RuntimeError(f"Error restoring database: {str(e)}")

    def _trigger_event(self, event_name: str, *args, **kwargs):
        """
        Trigger a database event.
        """
        trigger_event(event_name, *args, **kwargs)

    def execute_query(self, query: str, *args: Any) -> bool:
        """
        Execute a database query.

        Args:
            query (str): The SQL query to be executed.
            *args: Parameters to be passed to the query.

        Returns:
            bool: True if the query was successful, False otherwise.

        Raises:
            RuntimeError: If there is an error executing the query.
        """
        try:
            self.manager.cursor.execute(query, args)
            self.manager.connection.commit()
            self._trigger_event('insert_data', self.manager)
            return True
        except Exception as e:
            self.manager.connection.rollback()
            raise RuntimeError(f"Error executing query: {str(e)}")
        
    def list_tables(self) -> List[str]:
        """
        Get a list of all tables in the SQLite database.

        Returns:
            list: A list of table names.
        
        Raises:
            RuntimeError: If there is an error listing tables.
        """
        try:
            query = "SELECT name FROM sqlite_master WHERE type='table'"
            self.manager.cursor.execute(query)
            tables = self.manager.cursor.fetchall()
            return [table[0] for table in tables]
        except Exception as e:
            raise RuntimeError(f"Error listing tables: {str(e)}")

    def insert_base64(self, table_name: str, data_dict: Dict[str, Any]) -> None:
        """
        Insert base64 encoded data into a database table.

        Args:
            table_name (str): Name of the table to insert data into.
            data_dict (dict): A dictionary where keys are column names, and values are data to be encoded and inserted.

        Raises:
            RuntimeError: If there is an error inserting the data.
        """
        try:
            encoded_data_dict = {}
            for column, data in data_dict.items():
                if isinstance(data, str):
                    encoded_data_dict[column] = base64.b64encode(data.encode()).decode()
                else:
                    encoded_data_dict[column] = data

            columns = ', '.join(encoded_data_dict.keys())
            values = ', '.join(['?' for _ in encoded_data_dict])
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            self.execute_query(query, *encoded_data_dict.values())
        except Exception as e:
            raise RuntimeError(f"Error inserting base64 data: {str(e)}")

    def read_base64(self, table_name: str, only_base64: bool) -> List[Dict[str, Any]]:
        """
        Read and decode base64 encoded data from a database table.

        Args:
            table_name (str): Name of the table to read data from.
            only_base64 (bool): If True, only return rows where at least one column contains base64 encoded data.

        Returns:
            list: A list of dictionaries where keys are column names, and values are decoded data as bytes.

        Raises:
            RuntimeError: If there is an error selecting or decoding the data.
        """
        try:
            query = f"SELECT * FROM {table_name}"
            self.manager.cursor.execute(query)
            rows = self.manager.cursor.fetchall()

            if rows:
                column_names = [description[0] for description in self.manager.cursor.description]
                decoded_data = []
                for row in rows:
                    row_data = {}
                    for i in range(len(row)):
                        if isinstance(row[i], str):
                            try:
                                base64_decoded = base64.b64decode(row[i])
                                row_data[column_names[i]] = base64_decoded
                            except binascii.Error:
                                row_data[column_names[i]] = row[i] 
                        else:
                            try:
                                base64_decoded = base64.b64decode(str(row[i]))
                                row_data[column_names[i]] = base64_decoded
                            except (binascii.Error, TypeError):
                                row_data[column_names[i]] = row[i] 
                    if not only_base64:
                        decoded_data.append(row_data)
                    elif any(isinstance(value, bytes) for value in row_data.values()):
                        decoded_data.append(row_data)
                return decoded_data
            else:
                return None
        except Exception as e:
            raise RuntimeError(f"Error reading and decoding base64 data: {str(e)}")