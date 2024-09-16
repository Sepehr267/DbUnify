Manager
=========

This module is responsible for managing asynchronous database operations with MySQL.

.. automodule:: DbUnify.MySQL.aio.Manager.Manager
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------

**connect**

Connect to the MySQL database.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager

    async def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        await manager.connect()
        print("Connected to the database")

    asyncio.run(main())

**close**

Close the database connection.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager

    async def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        await manager.connect()
        await manager.close()
        print("Connection closed")

    asyncio.run(main())

**create_table**

Create a table in the database using `DataType` and `Rules` for column definitions.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager
    from DbUnify.MySQL.data import DataType, Rules

    async def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        await manager.connect()
        await manager.create_table(
        table_name='users',
        columns=[
            ('id', 'INT', ['PRIMARY KEY', 'AUTO_INCREMENT']),
            ('name', 'VARCHAR(100)', ['NOT NULL']),
            ('email', 'VARCHAR(100)', ['UNIQUE'])
        ])
        print("Table created")

    asyncio.run(main())

**drop_table**

Drop a table from the database.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager

    async def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        await manager.connect()
        await manager.drop_table('users')
        print("Table dropped")

    asyncio.run(main())

**add_column**

Add a column to an existing table using `DataType` and `Rules`.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager
    from DbUnify.MySQL.data import DataType, Rules

    async def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        await manager.connect()
        await manager.add_column(
            table_name='users',
            column_name='email',
            data_type=DataType.VARCHAR(255),
            constraints=Rules.UNIQUE
        )
        print("Column added")

    asyncio.run(main())

**delete_column**

Delete a column from a table.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager

    async def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        await manager.connect()
        await manager.delete_column('users', 'email')
        print("Column deleted")

    asyncio.run(main())

**insert_row**

Insert a row into a table.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager

    async def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        await manager.connect()
        await manager.insert_row(
            table_name='users',
            values={'name': 'John Doe'}
        )
        print("Row inserted")

    asyncio.run(main())

**delete_row**

Delete a row from a table based on a condition.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager

    async def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        await manager.connect()
        await manager.delete_row(
            table_name='users',
            condition='name = %s',
            'John Doe'
        )
        print("Row deleted")

    asyncio.run(main())

**update_row**

Update a row in the table based on a condition.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager

    async def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        await manager.connect()
        await manager.update_row(
            table_name='users',
            values={'email': 'JoneDoe@yahoo.com'},
            condition='name = John Doe'
        )
        print("Row updated")

    asyncio.run(main())

**select**

Select all rows from a table.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager

    async def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        await manager.connect()
        rows = await manager.select('users')
        print("Rows selected:", rows)

    asyncio.run(main())

**select_one**

Select a single row from a table based on a condition.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager

    async def main():
        manager = Manager(
            host='localhost',
            user='user',
            password='password',
            database='example_db',
            port=3306
        )
        await manager.connect()
        row = await manager.select_one('users', condition='name = John Doe')
        print("Row selected:", row)

    asyncio.run(main())