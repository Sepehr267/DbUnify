from typing import Tuple, Union, List
import mysql.connector
from mysql.connector import Error

class Raw:
    """
    The Raw class provides an interface for executing raw SQL queries on a MySQL database. It supports query execution with parameterized queries and fetching results.
    """

    def __init__(self, manager: 'Manager') -> None:
        """
        Initialize the Raw instance.
        
        Args:
            manager (Manager): An instance of the Manager class.
        """
        self.manager = manager

    def execute_query(self, query: str, *params: Union[str, int, float]) -> Union[List[Tuple], None]:
        """
        Execute a raw SQL query.
        
        Args:
            query (str): The SQL query to be executed.
            *params: Parameters to be passed to the query.
        
        Returns:
            list: List of fetched rows if it's a SELECT query.
            None: If it's an INSERT, UPDATE, or DELETE query.
        
        Raises:
            RuntimeError: If there is an error executing the query.
        """
        try:
            self.manager.cursor.execute(query, params)
            if query.strip().upper().startswith('SELECT'):
                return self.manager.cursor.fetchall()
            else:
                self.manager.connection.commit()
                return None
        except Error as e:
            raise RuntimeError(f"Error executing query: {str(e)}")

    def list_tables(self) -> List[str]:
        """
        List all tables in the database.

        Returns:
            List[str]: A list of table names.

        Raises:
            RuntimeError: If there is an error listing the tables.
        """
        try:
            self.manager.cursor.execute("SHOW TABLES")
            result = self.manager.cursor.fetchall() 
            tables = [row[0] for row in result]
            return tables
        except RuntimeError as e:
            raise RuntimeError(f"Error listing tables: {str(e)}")