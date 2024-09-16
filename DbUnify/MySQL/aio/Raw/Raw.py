from typing import Tuple, Union, List
import aiomysql

class Raw:
    """
    The Raw class provides an interface for executing raw SQL queries on a MySQL database asynchronously.
    It supports query execution with parameterized queries and fetching results.
    """

    def __init__(self, manager: 'Manager') -> None:
        """
        Initialize the Raw instance.
        
        Args:
            manager (Manager): An instance of the Manager class.
        """
        self.manager = manager

    async def execute_query(self, query: str, *params: Union[str, int, float]) -> Union[List[Tuple], None]:
        """
        Execute a raw SQL query asynchronously.
        """
        if not self.manager.connection:
            raise RuntimeError("Database connection not established.")
        
        try:
            async with self.manager.connection.cursor() as cursor:
                await cursor.execute(query, params)
                if query.strip().upper().startswith('SELECT'):
                    result = await cursor.fetchall()
                    return result
                else:
                    await self.manager.connection.commit()
                    return None
        except aiomysql.MySQLError as e:
            raise RuntimeError(f"Error executing query: {str(e)}")
    
    async def list_tables(self) -> List[str]:
        """
        List all tables in the database.

        Returns:
            List[str]: A list of table names.

        Raises:
            RuntimeError: If there is an error listing the tables.
        """
        try:
            async with self.manager.connection.cursor() as cursor:
                await cursor.execute('SHOW TABLES')
                result = await cursor.fetchall()
                tables = [row[0] for row in result]
                return tables
        except aiomysql.MySQLError as e:
            raise RuntimeError(f"Error listing tables: {str(e)}")
