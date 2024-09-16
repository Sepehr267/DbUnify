from typing import Dict, Type
import aiomysql
from .ORMException import ORMMException
from ..Manager.Manager import Manager
from ...Cache import Cache

class ORMManager(Manager):
    """
    ORMManager Class

    The ORMManager class provides methods for managing database schema and interactions using ORM (Object-Relational Mapping) principles.
    It extends the Manager class and includes functionalities for mapping models, applying migrations, and handling database resources.

    Attributes:
        cache (Cache): An instance of the Cache class for caching query results.
        connection (aiomysql.Connection): Asynchronous database connection.
        cursor (aiomysql.Cursor): Asynchronous database cursor.
    """

    def __init__(self, host: str, user: str, password: str, database: str, port: int = 3306, cache_ttl: int = 60) -> None:
        """
        Initialize the ORMManager instance.

        Args:
            host (str): The hostname of the MySQL database server.
            user (str): The username used to authenticate with the MySQL database.
            password (str): The password used to authenticate with the MySQL database.
            database (str): The name of the database.
            port (int): The port number for the MySQL database connection.
            cache_ttl (int): Time-to-live for cache entries in seconds. Default is 60 seconds (1 minute).
        """
        super().__init__(host, user, password, database, port, cache_ttl)
        self.cache_ttl = cache_ttl
        self.cache = Cache(ttl=cache_ttl)
        self.connection = None
        self.cursor = None

    async def __aenter__(self):
        """
        Enter the asynchronous runtime context related to this object.

        Returns:
            ORMManager: The ORMManager instance.
        """
        self.connection = await aiomysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.database
        )
        self.cursor = await self.connection.cursor()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the asynchronous runtime context related to this object.

        Args:
            exc_type (type): The type of exception if one occurred within the with block.
            exc_val (Exception): The value of the exception if one occurred within the with block.
            exc_tb (traceback): The traceback of the exception if one occurred within the with block.
        """
        await self._orm_exit()

    async def connect(self) -> None:
        """
        Establish a connection to the database and create a cursor.
        """
        self.connection = await aiomysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.database
        )
        self.cursor = await self.connection.cursor()

    async def get_table_columns(self, table_name: str) -> Dict[str, str]:
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
            query = f"DESCRIBE `{table_name}`"
            await self.cursor.execute(query)
            columns = await self.cursor.fetchall()
            return {col[0]: col[1] for col in columns}
        except Exception as e:
            raise ORMMException(f"Error getting table columns: {str(e)}")

    async def apply_migrations(self, model: Type['Model']) -> None:
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
            existing_columns = await self.get_table_columns(table_name)

            new_columns = []
            for field_name, field_obj in model_fields.items():
                if field_name not in existing_columns:
                    new_columns.append(f"ADD COLUMN `{field_name}` {field_obj.data_type} {field_obj.constraints}")
                elif existing_columns[field_name] != field_obj.data_type:
                    raise ORMMException(f"Data type mismatch for column '{field_name}' in table '{table_name}'")

            if new_columns:
                alter_query = f"ALTER TABLE `{table_name}` " + ", ".join(new_columns)
                await self.cursor.execute(alter_query)

            for existing_column in existing_columns:
                if existing_column not in model_fields:
                    await self.cursor.execute(f"ALTER TABLE `{table_name}` DROP COLUMN `{existing_column}`")

        except Exception as e:
            raise ORMMException(f"Error applying migrations: {str(e)}")

    async def map_model(self, model: Type['Model']) -> None:
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
            columns = [f"`{field_name}` {field_obj.data_type} {field_obj.constraints}" for field_name, field_obj in model.get_fields().items()]
            if not await self.table_exists(table_name):
                create_query = f"CREATE TABLE `{table_name}` (" + ", ".join(columns) + ")"
                await self.cursor.execute(create_query)
            else:
                await self.apply_migrations(model)
        except Exception as e:
            raise ORMMException(f"Error mapping model: {str(e)}")

    async def table_exists(self, table_name: str) -> bool:
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
            query = f"SHOW TABLES LIKE '{table_name}'"
            await self.cursor.execute(query)
            return await self.cursor.fetchone() is not None
        except Exception as e:
            raise ORMMException(f"Error checking if table exists: {str(e)}")

    async def _orm_exit(self) -> None:
        """
        A private method for closing resources and performing final cleanup.

        This method ensures that resources related to ORMManager are properly released and no resources are left open.
        """
        if self.cursor:
            await self.cursor.close()
        if self.connection:
            self.connection.close()

    async def close(self) -> None:
        """
        Close the database connection and cursor.
        """
        if self.cursor:
            await self.cursor.close()
        if self.connection:
            self.connection.close()

    async def execute_query(self, query: str, *params) -> None:
        """
        Execute a query with parameters and commit the transaction.

        Args:
            query (str): The SQL query to execute.
            *params: Parameters to pass to the query.

        Raises:
            ORMMException: If the cursor is not initialized.
        """
        if self.cursor is None:
            raise ORMMException("Cursor is not initialized.")
        await self.cursor.execute(query, params)
        await self.connection.commit()

    async def fetch_all(self, query: str, *params) -> list:
        """
        Execute a query and fetch all results.

        Args:
            query (str): The SQL query to execute.
            *params: Parameters to pass to the query.

        Returns:
            list: A list of tuples representing the query results.

        Raises:
            ORMMException: If the cursor is not initialized.
        """
        if self.cursor is None:
            raise ORMMException("Cursor is not initialized.")
        await self.cursor.execute(query, params)
        return await self.cursor.fetchall()
