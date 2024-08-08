from .ORMException import ORMMException
from ..Manager.Manager import Manager
from ...Cache import Cache
from typing import Dict, Type

class ORMManager(Manager):
    """
    ORMManager Class

    The ORMManager class provides methods for managing database schema and interactions using ORM (Object-Relational Mapping) principles. It extends the Manager class and includes functionalities for mapping models, applying migrations, and handling database resources.

    Attributes:
        cache (Cache): An instance of the Cache class for caching query results.

    Methods:
        __enter__(self): Enter the runtime context related to this object.
        __exit__(self, exc_type, exc_val, exc_tb): Exit the runtime context related to this object.
        get_table_columns(self, table_name): Get the columns and their data types for a table.
        apply_migrations(self, model): Apply migrations to the database schema based on the provided model.
        map_model(self, model): Map a model to a database table and create it if it doesn't exist.
        table_exists(self, table_name): Check if a table exists in the database.
        _orm_exit(self): A private method for closing resources and performing final cleanup.
    """
    
    def __init__(self, db_name: str, cache_ttl: int = 60) -> None:
        """
        Initialize the ORMManager instance.

        Args:
            cache_ttl (int): Time-to-live for cache entries in seconds. Default is 60 seconds (1 minute).
        """
        super().__init__(db_name, cache_ttl)
        self.cache_ttl = cache_ttl
        self.cache = Cache(ttl=cache_ttl)

    def __enter__(self):
        """
        Enter the runtime context related to this object.

        Returns:
            ORMManager: The ORMManager instance.
        """
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the runtime context related to this object.

        Args:
            exc_type (type): The type of exception if one occurred within the with block.
            exc_val (Exception): The value of the exception if one occurred within the with block.
            exc_tb (traceback): The traceback of the exception if one occurred within the with block.
        """
        self._orm_exit()

    def get_table_columns(self, table_name: str) -> Dict[str, str]:
        """
        Get the columns and their data types for a table.

        Args:
            table_name (str): Name of the table.

        Returns:
            dict: Dictionary of column names and their data types.

        Raises:
            ORMMException: If there is an error getting the columns.
        """
        try:
            self.cursor.execute(f"PRAGMA table_info({table_name})")
            columns = self.cursor.fetchall()
            return {col[1]: col[2] for col in columns}
        except Exception as e:
            raise ORMMException(f"Error getting table columns: {str(e)}")

    def apply_migrations(self, model: Type['Model']) -> None:
        """
        Apply migrations to the database schema based on the provided model.

        Args:
            model (Type[Model]): The model class used for applying migrations.

        Raises:
            ORMMException: If there is an error applying migrations.
        """
        from .Model import Model
        try:
            table_name = model.get_table_name()
            model_fields = model.get_fields()
            existing_columns = self.get_table_columns(table_name)

            new_columns = []
            for field_name, field_obj in model_fields.items():
                if field_name not in existing_columns:
                    new_columns.append((field_name, field_obj.data_type, field_obj.constraints))
                elif existing_columns[field_name] != field_obj.data_type:
                    raise ORMMException(f"Data type mismatch for column '{field_name}' in table '{table_name}'")
            
            if new_columns:
                self.add_columns(table_name, new_columns)
            
            for existing_column in existing_columns:
                if existing_column not in model_fields:
                    self.delete_column(table_name, existing_column)
        except Exception as e:
            raise ORMMException(f"Error applying migrations: {str(e)}")

    def map_model(self, model: Type['Model']) -> None:
        """
        Map a model to a database table and create it if it doesn't exist.

        Args:
            model (Type[Model]): The model class to be mapped to the database.

        Raises:
            ORMMException: If there is an error mapping the model.
        """
        from .Model import Model

        try:
            table_name = model.get_table_name()
            columns = [(field_name, field_obj.data_type, field_obj.constraints) for field_name, field_obj in model.get_fields().items()]
            if not self.table_exists(table_name):
                self.create_table(table_name, columns)
            else:
                self.apply_migrations(model)
        except Exception as e:
            raise ORMMException(f"Error mapping model: {str(e)}")

    def table_exists(self, table_name: str) -> bool:
        """
        Check if a table exists in the database.

        Args:
            table_name (str): Name of the table to check.

        Returns:
            bool: True if the table exists, False otherwise.

        Raises:
            ORMMException: If there is an error checking if the table exists.
        """
        try:
            self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
            return self.cursor.fetchone() is not None
        except Exception as e:
            raise ORMMException(f"Error checking if table exists: {str(e)}")
    
    def _orm_exit(self):
        """
        A private method for closing resources and performing final cleanup.

        This method ensures that resources related to ORMManager are properly released and no resources are left open.
        """
        if hasattr(self, 'connection') and self.connection:
            self.connection.close()
