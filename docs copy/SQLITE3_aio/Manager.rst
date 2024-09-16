Manager
=========

This module is responsible for managing asynchronous database operations.

.. automodule:: DbUnify.SQLite3.aio.Manager.Manager
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------

**connect**

Connect to the SQLite database.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager

    async def main():
        manager = Manager(db_name='example.db')
        await manager.connect()
        print("Connected to the database")

    asyncio.run(main())

**close**

Close the database connection.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager

    async def main():
        manager = Manager(db_name='example.db')
        await manager.connect()
        await manager.close() 
        print("Connection closed")

    asyncio.run(main())

**create_table**

Create a table in the database using `DataType` and `Rules` for column definitions.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager
    from DbUnify.SQLite3.data import DataType, Rules

    async def main():
        manager = Manager(db_name='example.db')
        await manager.connect()
        await manager.create_table(
            table_name='users',
            columns=[
                ('id', DataType.INTEGER, [Rules.PRIMARY_KEY]),
                ('name', DataType.TEXT, [Rules.NOT_NULL]),
            ]
        )

    asyncio.run(main())

**drop_table**

Drop a table from the database.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager

    async def main():
        manager = Manager(db_name='example.db')
        await manager.connect()
        await manager.drop_table('users')
        print("Table dropped")

    asyncio.run(main())

**add_column**

Add a column to an existing table using `DataType` and `Rules`.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager
    from DbUnify.SQLite3.data import DataType, Rules

    async def main():
        manager = Manager(db_name='example.db')
        await manager.connect()
        
        # NOTE: add_column not Support Rules
        await manager.add_column(
            table_name='users',
            column_name='email',
            data_type=DataType.TEXT
        )
        print("Column added")

    asyncio.run(main())

**delete_column**

Delete a column from a table.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager

    async def main():
        manager = Manager(db_name='example.db')
        await manager.connect()
        await manager.delete_column('users', 'email')
        print("Column deleted")

    asyncio.run(main())

**insert_row**

Insert a row into a table.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager

    async def main():
        manager = Manager(db_name='example.db')
        await manager.connect()
        await manager.insert_row(
                table_name='users',
                values={
                    'id': 1,
                    'name': 'John Doe'
                }
        )
        print("Row inserted")

    asyncio.run(main())

**delete_row**

Delete a row from a table based on a condition.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager

    async def main():
        manager = Manager(db_name='example.db')
        await manager.connect()
        await manager.delete_row(
            table_name='users',
            condition_column='name',
            condition_value='John Doe'
        )
        print("Row deleted")

    asyncio.run(main())

**update_row**

Update a row in the table based on a condition.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager

    async def main():
        manager = Manager(db_name='example.db')
        await manager.connect()
        await manager.update_row(
            table_name='users',
            values={'email': 'Jane Doe@gmail.com'},
            condition_column='name',
            condition_value='John Doe'
        )
        print("Row updated")

    asyncio.run(main())

**select**

Select all rows from a table.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager

    async def main():
        manager = Manager(db_name='example.db')
        await manager.connect()
        rows = await manager.select('users')
        print("Rows selected:", rows)

    asyncio.run(main())

**select_one**

Select a single row from a table based on a condition.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager

    async def main():
        manager = Manager(db_name='example.db')
        await manager.connect()
        row = await manager.select_one(
            table_name='users',
            name='John Doe'
        )
        print("Row selected:", row)

    asyncio.run(main())

**get_table_columns**

Get columns and their data types for a table.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager

    async def main():
        manager = Manager(db_name='example.db')
        await manager.connect()
        columns = await manager.get_table_columns('users')
        print("Table columns:", columns)

    asyncio.run(main())