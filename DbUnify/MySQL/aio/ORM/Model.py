from typing import Dict, List, Tuple, Optional, Union
from .Field import Field
from .ModelMeta import ModelMeta
from ...data.Rules import Rules
from .ORMManager import ORMMException

class Model(metaclass=ModelMeta):
    """
    Base class for all models, handling field definitions and schema management.
    """
    orm_manager = None

    def __init__(self, **kwargs):
        """
        Initialize the model with provided field values.

        Args:
            kwargs: Field values to initialize the model with.
        """ 
        for key, value in kwargs.items():
            if key in self._fields:
                setattr(self, key, value)

    @classmethod
    def set_manager(cls, manager) -> None:
        """
        Set the ORMManager instance for the model.

        Args:
            manager (ORMManager): The ORMManager instance to be used by the model.
        """
        cls.orm_manager = manager

    @classmethod
    def get_fields(cls) -> Dict[str, Field]:
        """
        Get the fields of the model.

        Returns:
            dict: A dictionary of field names and their definitions.
        """
        return cls._fields

    @classmethod
    def get_table_name(cls) -> str:
        """
        Get the table name for the model.

        Returns:
            str: The name of the table in lowercase.
        """
        return cls.__name__.lower()

    @classmethod
    async def create_table_schema(cls) -> str:
        """
        Generate the SQL schema for creating a table based on the model's fields.

        Returns:
            str: The SQL schema string for creating the table.
        """
        columns_definitions = [
            f"{field_name} {field.data_type} {' '.join([rule.value if isinstance(rule, Rules) else rule for rule in field.constraints])}"
            for field_name, field in cls.get_fields().items()
        ]
        if not columns_definitions:
            raise ORMMException("No fields defined for model.")

        return f"CREATE TABLE IF NOT EXISTS {cls.get_table_name()} ({', '.join(columns_definitions)})"

    @classmethod
    async def fetch_all(cls, query: str, *args) -> List[Tuple]:
        """
        Execute a query and fetch all results using the ORMManager instance.

        Args:
            query (str): The SQL query to execute.
            *args: Parameters for the query.

        Returns:
            List[Tuple]: The results of the query.
        
        Raises:
            ORMMException: If ORMManager instance is not set.
        """
        if cls.orm_manager is None:
            raise ORMMException("ORMManager instance is not set.")

        return await cls.orm_manager.fetch_all(query, *args)

    @classmethod
    async def create_table(cls) -> None:
        """
        Create the table in the database using the ORMManager instance.

        Raises:
            ORMMException: If ORMManager instance is not set.
        """
        if cls.orm_manager is None:
            raise ORMMException("ORMManager instance is not set.")

        schema = await cls.create_table_schema()
        await cls.orm_manager.raw.execute_query(schema)

    @classmethod
    async def drop_table(cls) -> None:
        """
        Drop the table from the database using the ORMManager instance.

        Raises:
            ORMMException: If ORMManager instance is not set.
        """
        if cls.orm_manager is None:
            raise ORMMException("ORMManager instance is not set.")

        await cls.orm_manager.drop_table(cls.get_table_name())

    @classmethod
    async def add_column(cls ,column_name: str, data_type: str, constraints: str) -> None:
        """
        Add a column to the table using the ORMManager instance.

        Args:
            column_name (str): Name of the column to be added.
            data_type (str): Data type of the column.
            constraints (str): Constraints to be applied on the column.

        Raises:
            ORMMException: If ORMManager instance is not set.
        """
        if cls.orm_manager is None:
            raise ORMMException("ORMManager instance is not set.")

        await cls.orm_manager.add_column(cls.get_table_name(), column_name, data_type, constraints)

    @classmethod
    async def insert_row(cls, values: Dict[str, Union[str, int, float]]) -> None:
        """
        Insert a row into the table using the ORMManager instance.

        Args:
            values (Dict[str, Union[str, int, float]]): The values to insert into the row.

        Raises:
            ORMMException: If ORMManager instance is not set.
        """
        if cls.orm_manager is None:
            raise ORMMException("ORMManager instance is not set.")

        await cls.orm_manager.insert_row(cls.get_table_name(), values)

    @classmethod
    async def delete_column(cls, column_name: str) -> None:
        """
        Delete a column from the table using the ORMManager instance.

        Args:
            column_name (str): The name of the column to delete.

        Raises:
            ORMMException: If ORMManager instance is not set.
        """
        if cls.orm_manager is None:
            raise ORMMException("ORMManager instance is not set.")

        query = f"ALTER TABLE `{cls.get_table_name()}` DROP COLUMN `{column_name}`"
        await cls.orm_manager.raw.execute_query(query)

    @classmethod
    async def delete_row(cls, **conditions) -> None:
        """
        Delete a row from the table based on a condition using the ORMManager instance.

        Args:
            conditions (Dict[str, Union[str, int, float]]): The conditions to identify which row(s) to delete.

        Raises:
            ORMMException: If ORMManager instance is not set.
            ValueError: If no conditions are provided.
        """
        if cls.orm_manager is None:
            raise ORMMException("ORMManager instance is not set.")

        if not conditions:
            raise ValueError("At least one condition must be provided.")

        condition_str = ' AND '.join(f"`{key}` = %s" for key in conditions)
        values = tuple(conditions.values())
        query = f"DELETE FROM `{cls.get_table_name()}` WHERE {condition_str}"
        await cls.orm_manager.raw.execute_query(query, *values)

    @classmethod
    async def update_row(cls, condition: str, **values) -> None:
        """
        Update a row in the table based on a condition using the ORMManager instance.

        Args:
            condition (str): The condition to identify which row(s) to update.
            values (Dict[str, Union[str, int, float]]): The values to update in the row.

        Raises:
            ORMMException: If ORMManager instance is not set.
        """
        if cls.orm_manager is None:
            raise ORMMException("ORMManager instance is not set.")

        update_expr = ', '.join(f"`{key}` = %s" for key in values)
        query = f"UPDATE `{cls.get_table_name()}` SET {update_expr} WHERE {condition}"
        await cls.orm_manager.raw.execute_query(query, *values.values())

    @classmethod
    async def select_one(cls, **conditions) -> Optional[Dict[str, Union[str, int, float]]]:
        """
        Search for a single row in the table based on a condition using the ORMManager instance.

        Args:
            conditions (Dict[str, Union[str, int, float]]): The conditions to identify the row to select.

        Returns:
            Optional[Dict[str, Union[str, int, float]]]: The selected row as a dictionary, or None if no row is found.

        Raises:
            ORMMException: If ORMManager instance is not set.
        """
        if cls.orm_manager is None:
            raise ORMMException("ORMManager instance is not set.")

        condition_clauses = [f"`{key}` = %s" for key in conditions]
        where_clause = " AND ".join(condition_clauses)
        query = f"SELECT * FROM `{cls.get_table_name()}` WHERE {where_clause}"
        result = await cls.orm_manager.fetch_all(query, *conditions.values())

        if result:
            columns = await cls.get_table_columns()
            return dict(zip(columns.keys(), result[0]))

        return None

    @classmethod
    async def select(cls) -> List[Dict[str, Union[str, int, float]]]:
        """
        Search for all rows in the table using the ORMManager instance.

        Returns:
            List[Dict[str, Union[str, int, float]]]: A list of dictionaries representing all rows in the table.

        Raises:
            ORMMException: If ORMManager instance is not set.
        """
        if cls.orm_manager is None:
            raise ORMMException("ORMManager instance is not set.")

        query = f"SELECT * FROM `{cls.get_table_name()}`"
        results = await cls.orm_manager.fetch_all(query)
        columns = await cls.get_table_columns()

        return [dict(zip(columns.keys(), row)) for row in results]

    @classmethod
    async def get_table_columns(cls) -> Dict[str, str]:
        """
        Get the columns and their data types for the table using the ORMManager instance.

        Returns:
            dict: Dictionary of column names and their data types.

        Raises:
            ORMMException: If ORMManager instance is not set.
        """
        if cls.orm_manager is None:
            raise ORMMException("ORMManager instance is not set.")

        return await cls.orm_manager.get_table_columns(cls.get_table_name())

    @classmethod
    async def map_model(cls) -> None:
        """
        Map the model to a database table and create it if it doesn't exist using the ORMManager instance.

        Raises:
            ORMMException: If ORMManager instance is not set.
        """
        if cls.orm_manager is None:
            raise ORMMException("ORMManager instance is not set.")

        table_name = cls.get_table_name()
        existing_columns = await cls.orm_manager.get_table_columns(table_name)

        for field_name, field_obj in cls._fields.items():
            if field_name not in existing_columns:
                await cls.orm_manager.add_column(table_name, field_name, field_obj.data_type, field_obj.constraints)

    @classmethod
    def get_orm_manager(cls):
        """
        Get the ORMManager instance for the model.

        Returns:
            ORMManager: The ORMManager instance.
        """
        from .ORMManager import ORMManager
        return cls.orm_manager
