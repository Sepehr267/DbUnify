from typing import Any, Dict, List
import base64
import binascii
import shutil
import asyncio
 
class Raw:
    """
    # Raw Class

    #### The Raw class provides methods for executing raw SQL queries, creating database backups, restoring backups,
    #### listing tables, inserting and reading base64 encoded data.

    ### Attributes:
        - manager (Manager): The Manager instance managing the database connection.

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

    async def backup_database(self, backup_path: str) -> bool:
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
            await asyncio.to_thread(shutil.copyfile, self.manager.db_name, backup_path)
            return True
        except Exception as e:
            raise RuntimeError(f"Error creating database backup: {str(e)}")
        
    async def restore_database(self, backup_path: str) -> bool:
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
            await asyncio.to_thread(shutil.copyfile, backup_path, self.manager.db_name)
            return True
        except Exception as e:
            raise RuntimeError(f"Error restoring database: {str(e)}")

    async def execute_query(self, query: str, *args: Any) -> bool:
        """
        Execute a database query.

        Args:
            query (str): The SQL query to be executed.
            *args: Parameters to be passed to the query.

        Raises:
            RuntimeError: If there is an error executing the query.
        """
        if not self.manager.connection:
            raise RuntimeError("Database connection is not initialized.")

        try:
            async with self.manager.connection.cursor() as cursor:
                await cursor.execute(query, args)
                await self.manager.connection.commit()
            return True
        except Exception as e:
            if self.manager.connection:
                await self.manager.connection.rollback()
            raise RuntimeError(f"Error executing query: {str(e)}")
        
    async def list_tables(self) -> List[str]:
        """
        Get a list of all tables in the SQLite database.

        Returns:
            list: A list of table names.
        
        Raises:
            RuntimeError: If there is an error listing tables.
        """
        try:
            async with self.manager.connection.cursor() as cursor:
                await cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                tables = await cursor.fetchall()
                return [table[0] for table in tables]
        except Exception as e:
            raise RuntimeError(f"Error listing tables: {str(e)}")
        