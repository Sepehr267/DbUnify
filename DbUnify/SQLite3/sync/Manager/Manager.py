from ...data.Rules import Rules
from ...Cache import Cache
from typing import List, Tuple, Dict, Union, Optional
import sqlite3

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
        - add_column(self, table_name, column_name, data_type): Adds a column to an existing table.
        - insert_row(self, table_name, values): Inserts a row into the table.
        - delete_column(self, table_name, column_name): Deletes a column from the table.
        - delete_row(self, table_name, condition): Deletes a row from the table based on a condition.
        - update_row(self, table_name, values, condition): Updates a row in the table based on a condition.
        - select_one(self, table_name, condition): Searches for a single row in the table based on a condition.
        - select(self, table_name): Searches for all rows in the table.
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
        self.connect()

    def connect(self) -> None:
        """
        Connect to the SQLite database.
        """
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
        except sqlite3.Error as e:
            raise ConnectionError(f"Error connecting to the database: {str(e)}")

    def fetch_all(self, query: str, *args) -> List[Tuple]:
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
        try:
            self.cursor.execute(query, args)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            raise RuntimeError(f"Error executing query: {str(e)}")

    def create_table(self, table_name: str, columns: List[Tuple[str, str, Optional[List[Union[str, Rules]]]]]) -> None:
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
            for col_name, data_type, rules in columns:
                rules_str = ' '.join(rule.value for rule in rules) if rules else ''
                columns_definitions.append(f"{col_name} {data_type} {rules_str}")
            query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns_definitions)})"
            self.raw.execute_query(query)
        except sqlite3.Error as e:
            raise RuntimeError(f"Error creating table: {str(e)}")

    def drop_table(self, table_name: str) -> None:
        """
        Drop a table from the database.
        
        Args:
            table_name (str): Name of the table to be dropped.
        
        Raises:
            RuntimeError: If there is an error dropping the table.
        """
        try:
            query = f"DROP TABLE IF EXISTS {table_name}"
            self.raw.execute_query(query)
        except sqlite3.Error as e:
            raise RuntimeError(f"Error dropping table: {str(e)}")

    def add_column(self, table_name: str, column_name: str, data_type: str, constraints: str) -> None:
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
        try:
            self.raw.execute_query(query)
        except sqlite3.Error as e:
            raise RuntimeError(f"Error adding column: {str(e)}")

    def insert_row(self, table_name: str, values: Dict[str, Union[str, int, float]]) -> None:
        """
        Insert a row into the table.
        
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
            self.raw.execute_query(query, *values.values())
        except sqlite3.Error as e:
            raise RuntimeError(f"Error inserting row: {str(e)}")

    def delete_column(self, table_name: str, column_name: str) -> None:
        """
        Delete a column from the table.
        
        Args:
            table_name (str): Name of the table.
            column_name (str): Name of the column to be deleted.
        
        Raises:
            RuntimeError: If there is an error deleting the column.
        """
        try:
            temp_table_name = f"{table_name}_temp"
            current_columns = self.get_table_columns(table_name)
            columns_to_keep = [col for col in current_columns if col != column_name]

            columns_definitions = ', '.join([f"{col} {current_columns[col]}" for col in columns_to_keep])
            self.raw.execute_query(f"CREATE TABLE {temp_table_name} ({columns_definitions})")

            columns_names = ', '.join(columns_to_keep)
            self.raw.execute_query(f"INSERT INTO {temp_table_name} SELECT {columns_names} FROM {table_name}")

            self.drop_table(table_name)
            self.raw.execute_query(f"ALTER TABLE {temp_table_name} RENAME TO {table_name}")
        except sqlite3.Error as e:
            raise RuntimeError(f"Error deleting column: {str(e)}")

    def delete_row(self, table_name: str, condition: str, *args) -> None:
        """
        Delete a row from the table based on a condition.
        
        Args:
            table_name (str): Name of the table.
            condition (str): SQL condition to match rows to be deleted.
            *args: Parameters to be passed to the condition.
        
        Raises:
            RuntimeError: If there is an error deleting the row.
        """
        try:
            query = f"DELETE FROM {table_name} WHERE {condition}"
            self.raw.execute_query(query, *args)
        except sqlite3.Error as e:
            raise RuntimeError(f"Error deleting row: {str(e)}")

    def update_row(self, table_name: str, values: Dict[str, Union[str, int, float]], condition: str, *args) -> None:
        """
        Update a row in the table based on a condition.
        
        Args:
            table_name (str): Name of the table.
            values (dict): Dictionary of column-value pairs for the update.
            condition (str): SQL condition to match the row to be updated.
            *args: Parameters to be passed to the condition.
        
        Raises:
            RuntimeError: If there is an error updating the row.
        """
        try:
            set_clause = ', '.join([f"{col} = ?" for col in values])
            query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
            self.raw.execute_query(query, *values.values(), *args)
        except sqlite3.Error as e:
            raise RuntimeError(f"Error updating row: {str(e)}")

    def select_one(self, table_name: str, condition: str, *args) -> Optional[Dict[str, Union[str, int, float]]]:
        """
        Search for a single row in the table based on a condition.
        
        Args:
            table_name (str): Name of the table.
            condition (str): SQL condition to match the row.
            *args: Parameters to be passed to the condition.
        
        Returns:
            dict: The matched row as a dictionary of column-value pairs, or None if no row is found.
        
        Raises:
            RuntimeError: If there is an error searching for the row.
        """
        try:
            query = f"SELECT * FROM {table_name} WHERE {condition}"
            result = self.fetch_all(query, *args)
            if result:
                columns = self.get_table_columns(table_name)
                return dict(zip(columns.keys(), result[0]))
            return None
        except sqlite3.Error as e:
            raise RuntimeError(f"Error searching for row: {str(e)}")

    def select(self, table_name: str) -> List[Dict[str, Union[str, int, float]]]:
        """
        Search for all rows in the table.
        
        Args:
            table_name (str): Name of the table.
        
        Returns:
            list: List of rows, each as a dictionary of column-value pairs.
        
        Raises:
            RuntimeError: If there is an error searching for rows.
        """
        try:
            query = f"SELECT * FROM {table_name}"
            results = self.fetch_all(query)
            columns = self.get_table_columns(table_name)
            return [dict(zip(columns.keys(), row)) for row in results]
        except sqlite3.Error as e:
            raise RuntimeError(f"Error searching for rows: {str(e)}")

    def get_table_columns(self, table_name: str) -> Dict[str, str]:
        """
        Get the columns and their data types for a table.
        
        Args:
            table_name (str): Name of the table.
        
        Returns:
            dict: Dictionary of column names and their data types.
        
        Raises:
            RuntimeError: If there is an error getting the columns.
        """
        try:
            self.cursor.execute(f"PRAGMA table_info({table_name})")
            columns = self.cursor.fetchall()
            return {col[1]: col[2] for col in columns}
        except sqlite3.Error as e:
            raise RuntimeError(f"Error getting table columns: {str(e)}")

    def close(self) -> None:
        """
        Close the database connection.
        
        Raises:
            ConnectionError: If there is an error closing the connection.
        """
        try:
            if self.connection:
                self.connection.close()
                self.connection = None
                self.cursor = None
        except sqlite3.Error as e:
            raise ConnectionError(f"Error closing the database connection: {str(e)}")