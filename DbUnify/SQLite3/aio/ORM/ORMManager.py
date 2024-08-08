from typing import Dict, Type, Optional
from .ORMException import ORMMException
from ..Manager.Manager import Manager
import aiosqlite

class ORMManager(Manager):
    async def __aenter__(self):
        """
        This method is called when entering the `async with` block.
        It returns the instance of `ORMManager` (i.e., `self`) so that it can be used within the `async with` block.
        """
        self.connection = await aiosqlite.connect(self.db_name)
        self.cursor = await self.connection.cursor()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        This method is called when exiting the `async with` block.
        It invokes the `_orm_exit` method to handle resource cleanup and finalization.    
       
        Args:
            exc_type (type): The type of exception if one occurred within the `async with` block.
            exc_val (Exception): The value of the exception if one occurred within the `async with` block.
            exc_tb (traceback): The traceback of the exception if one occurred within the `async with` block.
        """
        if self.connection:
            await self.connection.close()

    def __init__(self, db_name: str, cache_ttl: int = 300) -> None:
        super().__init__(db_name, cache_ttl)

    async def get_table_columns(self, table_name: str) -> Dict[str, str]:
        """
        Get the columns and their data types for a table asynchronously.

        Args:
            table_name (str): Name of the table.

        Returns:
            dict: Dictionary of column names and their data types.

        Raises:
            ORMMException: If there is an error getting the columns.
        """
        try:
            async with self.connection.cursor() as cursor:
                await cursor.execute(f"PRAGMA table_info({table_name})")
                columns = await cursor.fetchall()
                return {col[1]: col[2] for col in columns}
        except Exception as e:
            raise ORMMException(f"Error getting table columns: {str(e)}")

    async def apply_migrations(self, model: Type['Model']) -> None:
        """
        Apply migrations to the database schema based on the provided model asynchronously.

        Args:
            model (Type[Model]): The model class used for applying migrations.

        Raises:
            ORMMException: If there is an error applying migrations.
        """
        from .Model import Model

        try:
            table_name = model.get_table_name()
            model_fields = model.get_fields()
            existing_columns = await self.get_table_columns(table_name)
            
            for field_name, field_obj in model_fields.items():
                if field_name not in existing_columns:
                    await self.add_column(table_name, field_name, field_obj.data_type, field_obj.constraints)
                elif existing_columns[field_name] != field_obj.data_type:
                    raise ORMMException(f"Data type mismatch for column '{field_name}' in table '{table_name}'")
            
            for existing_column in existing_columns:
                if existing_column not in model_fields:
                    await self.delete_column(table_name, existing_column)
        except Exception as e:
            raise ORMMException(f"Error applying migrations: {str(e)}")

    async def map_model(self, model: Type['Model']) -> None:
        """
        Map a model to a database table and create it if it doesn't exist asynchronously.

        Args:
            model (Type[Model]): The model class to be mapped to the database.

        Raises:
            ORMMException: If there is an error mapping the model.
        """
        from .Model import Model

        try:
            table_name = model.get_table_name()
            columns = [(field_name, field_obj.data_type, field_obj.constraints) for field_name, field_obj in model.get_fields().items()]
            if not await self.table_exists(table_name):
                await self.create_table(table_name, columns)
            else:
                await self.apply_migrations(model)
        except Exception as e:
            raise ORMMException(f"Error mapping model: {str(e)}")

    async def table_exists(self, table_name: str) -> bool:
        """
        Check if a table exists in the database asynchronously.

        Args:
            table_name (str): Name of the table to check.

        Returns:
            bool: True if the table exists, False otherwise.

        Raises:
            ORMMException: If there is an error checking if the table exists.
        """
        try:
            async with self.connection.cursor() as cursor:
                await cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
                return await cursor.fetchone() is not None
        except Exception as e:
            raise ORMMException(f"Error checking if table exists: {str(e)}")
    
    async def _orm_exit(self):
        """
        A private method for closing resources and performing final cleanup asynchronously.
        This method should be implemented to ensure that resources related to `ORMManager`
        are properly released and no resources are left open.
        """
        if hasattr(self, 'connection') and self.connection:
            await self.connection.close()
