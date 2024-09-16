from typing import List, Tuple, Dict, Union, Optional
from asyncio import get_event_loop
from ...Cache import Cache
from ...data import *
from ....SQL.SQLInjection import SQLInjection
import logging
import aiomysql

logging.basicConfig(filename='sql_errors.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class Manager:
    """
    Manager Class:

    The Manager class provides an interface for managing MySQL databases asynchronously. It offers methods for connecting to the database, executing SQL queries, creating and modifying tables, inserting and deleting rows, and closing the database connection.

    Attributes:
        host (str): The hostname of the MySQL database server.
        user (str): The username used to authenticate with the MySQL database.
        password (str): The password used to authenticate with the MySQL database.
        database (str): The name of the database.
        port (int): The port number for the MySQL database connection.
        connection: The connection object to the MySQL database.
        cursor: The cursor object for executing SQL queries.
        cache (Cache): An instance of the Cache class for caching query results.
        sql_injection_detection (bool): Enable or disable SQL injection detection.
        sql_injection_detector (SQLInjection): An instance of the SQLInjection class for detecting SQL injection.

    Methods:
        __init__(self, host, user, password, database, port, cache_ttl=300, sql_injection_detection=False): Initializes the Manager instance with MySQL database credentials.
        connect(self): Connects to the MySQL database.
        fetch_all(self, query, *args): Executes a query and fetches all results.
        create_table(self, table_name, columns): Creates a table in the database.
        drop_table(self, table_name): Drops a table from the database.
        add_column(self, table_name, column_name, data_type, constraints): Adds a column to an existing table.
        insert_row(self, table_name, values): Inserts a row into the table.
        delete_column(self, table_name, column_name): Deletes a column from the table.
        delete_row(self, table_name, condition): Deletes a row from the table based on a condition.
        update_row(self, table_name, values, condition): Updates a row in the table based on a condition.
        select_one(self, table_name, condition): Searches for a single row in the table based on a condition.
        select(self, table_name): Searches for all rows in the table.
        close(self): Closes the database connection.
    """

    def __init__(self, host: str, user: str, password: str, database: str, port: int, cache_ttl: int = 300, sql_injection_detection: bool = False) -> None:
        """
        Initialize the Manager instance.

        Args:
            host (str): The hostname of the MySQL database server.
            user (str): The username used to authenticate with the MySQL database.
            password (str): The password used to authenticate with the MySQL database.
            database (str): The name of the database.
            port (int): The port number for the MySQL database connection.
            cache_ttl (int): Time-to-live for cache entries in seconds. Default is 300 seconds (5 minutes).
            sql_injection_detection (bool): Enable or disable SQL injection detection. Default is False.
        """
        from ..Raw import Raw
        
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.cache = Cache(ttl=cache_ttl)
        self.connection = None
        self.cursor = None
        self.sql_injection_detection = sql_injection_detection
        self.sql_injection_detector = SQLInjection() if sql_injection_detection else None
        self.raw = Raw(self)
        self.loop = get_event_loop()

    async def connect(self) -> None:
        """
        Connect to the MySQL database.
        """
        from ..Raw import Raw
        try:
            self.connection = await aiomysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                db=self.database,
                autocommit=True
            )
            self.raw = Raw(self)
        except aiomysql.MySQLError as e:
            raise ConnectionError(f"Error connecting to the database: {str(e)}")

    def _check_for_injection(self, query: str, *args) -> bool:
        """
        Checks the query for potential SQL injection patterns if detection is enabled.

        Args:
            query (str): The SQL query to check.

        Returns:
            bool: True if potential SQL injection is detected, False otherwise.
        """
        if self.sql_injection_detection and self.sql_injection_detector:
            check = self.sql_injection_detector.detect(query, *args)
            if check:
                logging.error(f"Potential SQL injection detected. SQL Command: {query}, Parameters: {args}")
                return True
        return False

    async def fetch_all(self, query: str, *args) -> List[Tuple]:
        """
        Execute a query and fetch all results.
        
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
            async with self.connection.cursor() as cursor:
                await cursor.execute(query, args)
                return await cursor.fetchall()
        except aiomysql.MySQLError as e:
            logging.error(f"Error executing query: {str(e)}")
            raise RuntimeError(f"Error executing query: {str(e)}")

    async def create_table(self, table_name: str, columns: List[Tuple[str, str, Optional[List[Union[str, Rules]]]]]) -> None:
        """
        Create a table in the database.
        
        Args:
            table_name (str): Name of the table to be created.
            columns (list): List of tuples containing column names, data types, and rules.
        
        Raises:
            RuntimeError: If there is an error creating the table.
        """
        try:
            columns_definitions = []
            column_defs = []
            for name, data_type, rules in columns:
                rules_str = ' '.join(rules) if rules else ''
                column_defs.append(f"{name} {data_type} {rules_str}")
            columns_str = ', '.join(column_defs)
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})"
            if self._check_for_injection(query):
                return
            await self.raw.execute_query(query)
        except aiomysql.MySQLError as e:
            logging.error(f"Error creating table: {str(e)}")
            raise RuntimeError(f"Error creating table: {str(e)}")
    
    async def drop_table(self, table_name: str) -> None:
        """
        Drop a table from the database.
        
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
        except aiomysql.MySQLError as e:
            logging.error(f"Error dropping table: {str(e)}")
            raise RuntimeError(f"Error dropping table: {str(e)}")

    async def add_column(self, table_name: str, column_name: str, data_type: str, constraints: str) -> None:
        """
        Add a column to an existing table.
        
        Args:
            table_name (str): Name of the table to add the column to.
            column_name (str): Name of the column to be added.
            data_type (str): Data type of the column.
            constraints (str): Constraints to be applied on the column.
        
        Raises:
            RuntimeError: If there is an error adding the column.
        """
        query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type} {constraints}"
        if self._check_for_injection(query):
            return
        try:
            await self.raw.execute_query(query)
        except aiomysql.MySQLError as e:
            logging.error(f"Error adding column: {str(e)}")
            raise RuntimeError(f"Error adding column: {str(e)}")

    async def insert_row(self, table_name: str, values: Dict[str, Union[str, int, float]]) -> None:
        """
        Insert a row into the table.
        
        Args:
            table_name (str): Name of the table to insert the row into.
            values (dict): Dictionary of column-value pairs for the row.
        
        Raises:
            RuntimeError: If there is an error inserting the row.
        """
        columns = ', '.join(values.keys())
        placeholders = ', '.join(['%s' for _ in values])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        if self._check_for_injection(query, *values.values()):
            return
        try:
            await self.raw.execute_query(query, *values.values())
        except aiomysql.MySQLError as e:
            logging.error(f"Error inserting row: {str(e)}")
            raise RuntimeError(f"Error inserting row: {str(e)}")

    async def delete_column(self, table_name: str, column_name: str) -> None:
        """
        Delete a column from the table.
        
        Args:
            table_name (str): Name of the table to delete the column from.
            column_name (str): Name of the column to be deleted.
        
        Raises:
            RuntimeError: If there is an error deleting the column.
        """
        query = f"ALTER TABLE {table_name} DROP COLUMN {column_name}"
        if self._check_for_injection(query):
            return
        try:
            await self.raw.execute_query(query)
        except aiomysql.MySQLError as e:
            logging.error(f"Error deleting column: {str(e)}")
            raise RuntimeError(f"Error deleting column: {str(e)}")

    async def delete_row(self, table_name: str, condition: str) -> None:
        """
        Delete a row from the table based on a condition.
        
        Args:
            table_name (str): Name of the table to delete the row from.
            condition (str): Condition to identify the row(s) to be deleted.
        
        Raises:
            RuntimeError: If there is an error deleting the row.
        """
        if "=" in condition:
            field, value = condition.split("=", 1)
            field = field.strip()
            value = value.strip()
        
            if not (value.startswith("'") and value.endswith("'")):
                value = f"'{value}'"
        
            condition = f"{field} = {value}"
    
        query = f"DELETE FROM {table_name} WHERE {condition}"
        
        if self._check_for_injection(query):
            return
        try:
            await self.raw.execute_query(query)
        except aiomysql.MySQLError as e:
            logging.error(f"Error deleting row: {str(e)}")
            raise RuntimeError(f"Error deleting row: {str(e)}")

    async def update_row(self, table_name: str, values: Dict[str, Union[str, int, float]], condition: str) -> None:
        """
        Update a row in the table based on a condition.
        
        Args:
            table_name (str): Name of the table to update.
            values (dict): Dictionary of column-value pairs for the update.
            condition (str): Condition to identify the row(s) to be updated.
        
        Raises:
            RuntimeError: If there is an error updating the row.
        """
        set_clause = ', '.join([f"{k} = %s" for k in values.keys()])
    
        if "=" in condition:
            field, value = condition.split("=", 1)
            field = field.strip()
            value = value.strip()
        
            if not (value.startswith("'") and value.endswith("'")):
                value = f"'{value}'"
        
            condition = f"{field} = {value}"
    
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
    
        parameters = list(values.values())
    
        try:
            await self.raw.execute_query(query, *parameters)
        except aiomysql.MySQLError as e:
            logging.error(f"Error updating row: {str(e)}")
            raise RuntimeError(f"Error updating row: {str(e)}")

    async def select_one(self, table_name: str, condition: str) -> Optional[Tuple]:
        """
        Search for a single row in the table based on a condition.
        
        Args:
            table_name (str): Name of the table to search in.
            condition (str): Condition to identify the row.
        
        Returns:
            tuple: The found row, or None if no row is found.
        
        Raises:
            RuntimeError: If there is an error selecting the row.
        """
        if "=" in condition:
            field, value = condition.split("=", 1)
            field = field.strip()
            value = value.strip()
        
            if not (value.startswith("'") and value.endswith("'")):
                value = f"'{value}'"
        
            condition = f"{field} = {value}"

        query = f"SELECT * FROM {table_name} WHERE {condition}"
        
        if self._check_for_injection(query):
            return None
        try:
            result = await self.fetch_all(query)
            return result[0] if result else None
        except RuntimeError as e:
            logging.error(f"Error selecting row: {str(e)}")
            raise RuntimeError(f"Error selecting row: {str(e)}")

    async def select(self, table_name: str) -> List[Tuple]:
        """
        Search for all rows in the table.
        
        Args:
            table_name (str): Name of the table to search in.
        
        Returns:
            list: List of rows found in the table.
        
        Raises:
            RuntimeError: If there is an error selecting rows.
        """
        query = f"SELECT * FROM {table_name}"
        if self._check_for_injection(query):
            return []
        try:
            return await self.fetch_all(query)
        except RuntimeError as e:
            logging.error(f"Error selecting rows: {str(e)}")
            raise RuntimeError(f"Error selecting rows: {str(e)}")
    
    async def get_table_columns(self, table_name: str) -> Dict[str, str]:
        """
        Get the columns and their data types for a table.

        Args:
            table_name (str): Name of the table.

        Returns:
            dict: Dictionary of column names and their data types.
        """
        try:
            async with self.connection.cursor() as cursor:
                await cursor.execute(f'DESCRIBE `{table_name}`')
                return await cursor.fetchall()
                        
        except Exception as e:
            logging.error(f"Error get table columns : {str(e)}")
            raise RuntimeError(f"Error get table columns : {str(e)}")
        
    async def close(self) -> None:
        """
        Close the database connection.
        """
        self.connection.close()
