from ...data.Rules import Rules
from ..Cache import Cache
from typing import List, Tuple, Dict, Union, Optional
import aiosqlite

class Manager:
    """
    # Manager Class:
    
    #### The Manager class provides an interface for managing SQLite databases asynchronously. It offers methods for connecting to the database, executing SQL queries, creating and modifying tables, inserting and deleting rows, and closing the database connection.
    
    ### Attributes:
        - db_name (str): The name of the SQLite database.
        - raw (Raw): An instance of the Raw class for executing raw SQL queries.
        - connection: The connection object to the SQLite database.
        - cursor: The cursor object for executing SQL queries.
        - cache (Cache): An instance of the Cache class for caching query results.
    
    ### Methods:
        - __init__(self, db_name): Initializes the Manager instance with the name of the SQLite database.
        - connect(self): Asynchronously connects to the SQLite database.
        - fetch_all(self, query, *args): Executes a query and fetches all results.
        - create_table(self, table_name, columns): Creates a table in the database.
        - drop_table(self, table_name): Drops a table from the database.
        - add_column(self, table_name, column_name, data_type, constraints): Adds a column to an existing table.
        - insert_row(self, table_name, values): Inserts a row into the table.
        - delete_column(self, table_name, column_name): Deletes a column from the table.
        - delete_row(self, table_name, condition): Deletes a row from the table based on a condition.
        - update_row(self, table_name, values, condition): Updates a row in the table based on a condition.
        - select_one(self, table_name, condition): Searches for a single row in the table based on a condition.
        - select(self, table_name): Searches for all rows in the table.
        - get_table_columns(self, table_name): Gets columns and their data types for a table.
        - close(self): Closes the database connection.
    
    ### Raises:
        - ConnectionError: If there is an error connecting to or closing the database.
        - RuntimeError: If there is an error executing SQL queries, creating or modifying tables, inserting or deleting rows, or searching for rows.
    
    ### Note:
        - The 'Raw' class is used internally for executing raw SQL queries.
    """
    
    def __init__(self, db_name: str, cache_ttl: int = 300) -> None:
        """
        Initialize the Manager instance.

        Args:
            db_name (str): The name of the SQLite database.
            cache_ttl (int): Time-to-live for cache entries in seconds. Default is 300 seconds (5 minutes).
        """
        from ..Raw.Raw import Raw
        self.db_name = db_name
        self.cache = Cache(ttl=cache_ttl)
        self.connection = None
        self.cursor = None
        self.raw = Raw(self)
    
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
        try:
            await self.cursor.execute(query, args)
            return await self.cursor.fetchall()
        except aiosqlite.Error as e:
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
            await self.raw.execute_query(query)
        except aiosqlite.Error as e:
            raise RuntimeError(f"Error creating table: {str(e)}")

    async def drop_table(self, table_name: str) -> None:
        """
        Drop a table from the database asynchronously.
        
        Args:
            table_name (str): Name of the table to be dropped.

        Raises:
            RuntimeError: If there is an error dropping the table.
        """
        try:
            query = f"DROP TABLE IF EXISTS {table_name}"
            await self.raw.execute_query(query)
        except aiosqlite.Error as e:
            raise RuntimeError(f"Error dropping table: {str(e)}")

    async def add_column(self, table_name: str, column_name: str, data_type: str, constraints: str) -> None:
        """
        Add a column to an existing table asynchronously.
        
        Args:
            table_name (str): Name of the table to add the column to.
            column_name (str): Name of the column to be added.
            data_type (str): Data type of the column.
            constraints (str): Constraints to be applied on the column.

        Raises:
            RuntimeError: If there is an error adding the column.
        """
        try:
            query = f"ALTER TABLE {table_name} ADD COLUMN {column_name} {data_type} {constraints}"
            await self.raw.execute_query(query)
        except aiosqlite.Error as e:
            raise RuntimeError(f"Error adding column: {str(e)}")

    async def insert_row(self, table_name: str, values: Dict[str, Union[str, int, float]]) -> None:
        """
        Insert a row into the table asynchronously.
        
        Args:
            table_name (str): Name of the table to insert the row into.
            values (dict): Dictionary of column-value pairs for the row.

        Raises:
            RuntimeError: If there is an error inserting the row.
        """
        try:
            columns = ', '.join(values.keys())
            placeholders = ', '.join(['?' for _ in values])
            query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            await self.raw.execute_query(query, *values.values())
        except aiosqlite.Error as e:
            raise RuntimeError(f"Error inserting row: {str(e)}")

    async def delete_column(self, table_name: str, column_name: str) -> None:
        """
        Delete a column from the table asynchronously.
        
        Args:
            table_name (str): Name of the table.
            column_name (str): Name of the column to be deleted.

        Raises:
            RuntimeError: If there is an error deleting the column.
        """
        try:
            temp_table_name = f"{table_name}_temp"
            current_columns = await self.get_table_columns(table_name)
            columns_to_keep = [col for col in current_columns if col != column_name]

            columns_definitions = ', '.join([f"{col} {current_columns[col]}" for col in columns_to_keep])
            query = f"CREATE TABLE {temp_table_name} ({columns_definitions})"
            await self.raw.execute_query(query)

            columns_names = ', '.join(columns_to_keep)
            query = f"INSERT INTO {temp_table_name} SELECT {columns_names} FROM {table_name}"
            await self.raw.execute_query(query)

            await self.drop_table(table_name)
            query = f"ALTER TABLE {temp_table_name} RENAME TO {table_name}"
            await self.raw.execute_query(query)
        except aiosqlite.Error as e:
            raise RuntimeError(f"Error deleting column: {str(e)}")

    async def delete_row(self, table_name: str, condition: str, *args) -> None:
        """
        Delete a row from the table based on a condition asynchronously.
        
        Args:
            table_name (str): Name of the table.
            condition (str): SQL condition to match rows to be deleted.
            *args: Parameters to be passed to the condition.

        Raises:
            RuntimeError: If there is an error deleting the row.
        """
        try:
            query = f"DELETE FROM {table_name} WHERE {condition}"
            await self.raw.execute_query(query, *args)
        except aiosqlite.Error as e:
            raise RuntimeError(f"Error deleting row: {str(e)}")

    async def update_row(self, table_name: str, values: Dict[str, Union[str, int, float]], condition: str, *args) -> None:
        """
        UpdateHere's the continuation of the asynchronous `Manager` class:
        Update a row in the table based on a condition asynchronously.
        
        Args:
            table_name (str): Name of the table.
            values (dict): Dictionary of column-value pairs for the row to be updated.
            condition (str): SQL condition to match rows to be updated.
            *args: Parameters to be passed to the condition.

        Raises:
            RuntimeError: If there is an error updating the row.
        """
        try:
            set_clause = ', '.join([f"{col} = ?" for col in values.keys()])
            query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
            await self.raw.execute_query(query, *values.values(), *args)
        except aiosqlite.Error as e:
            raise RuntimeError(f"Error updating row: {str(e)}")

    async def select_one(self, table_name: str, condition: str, *args) -> Optional[Tuple]:
        """
        Search for a single row in the table based on a condition asynchronously.
        
        Args:
            table_name (str): Name of the table.
            condition (str): SQL condition to match the row.
            *args: Parameters to be passed to the condition.

        Returns:
            tuple: The fetched row if found, otherwise None.

        Raises:
            RuntimeError: If there is an error searching for the row.
        """
        try:
            query = f"SELECT * FROM {table_name} WHERE {condition}"
            rows = await self.fetch_all(query, *args)
            return rows[0] if rows else None
        except aiosqlite.Error as e:
            raise RuntimeError(f"Error selecting row: {str(e)}")

    async def select(self, table_name: str) -> List[Tuple]:
        """
        Search for all rows in the table asynchronously.
        
        Args:
            table_name (str): Name of the table.

        Returns:
            list: List of all rows in the table.

        Raises:
            RuntimeError: If there is an error selecting rows.
        """
        try:
            query = f"SELECT * FROM {table_name}"
            return await self.fetch_all(query)
        except aiosqlite.Error as e:
            raise RuntimeError(f"Error selecting rows: {str(e)}")

    async def get_table_columns(self, table_name: str) -> Dict[str, str]:
        """
        Get columns and their data types for a table asynchronously.
        
        Args:
            table_name (str): Name of the table.

        Returns:
            dict: Dictionary of column names and their data types.

        Raises:
            RuntimeError: If there is an error retrieving columns.
        """
        try:
            query = f"PRAGMA table_info({table_name})"
            columns_info = await self.fetch_all(query)
            return {row[1]: row[2] for row in columns_info}
        except aiosqlite.Error as e:
            raise RuntimeError(f"Error getting table columns: {str(e)}")

    async def close(self) -> None:
        """
        Close the database connection asynchronously.
        """
        try:
            if self.connection:
                await self.connection.close()
        except aiosqlite.Error as e:
            raise ConnectionError(f"Error closing the database: {str(e)}")