Raw
===

This module handles raw database interactions in asynchronous contexts.

.. automodule:: DbUnify.SQLite3.aio.Raw.Raw
   :members:
   :undoc-members:
   :show-inheritance:


Examples
--------------------

First, import the necessary modules and initialize the `Raw` class.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager
    from DbUnify.SQLite3.aio.Raw import Raw

    async def main():
        manager = Manager(db_name='database.db')
        raw = Raw(manager)

    asyncio.run(main())

**Create a Database Backup**

Create a backup of the database.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager
    from DbUnify.SQLite3.aio.Raw import Raw

    async def backup():
        manager = Manager(db_name='database.db')
        raw = Raw(manager)
        success = await raw.backup_database('backup.db')
        print("Backup successful:", success)

    asyncio.run(backup())

**Restore a Database from Backup**

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager
    from DbUnify.SQLite3.aio.Raw import Raw

    async def restore():
        manager = Manager(db_name='database.db')
        raw = Raw(manager)
        success = await raw.restore_database('backup.db')
        print("Restore successful:", success)

    asyncio.run(restore())

**Execute a SQL Query**

Execute a raw SQL query.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager
    from DbUnify.SQLite3.aio.Raw import Raw

    async def execute_query():
        manager = Manager(db_name='database.db')
        raw = Raw(manager)
        success = await raw.execute_query("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)")
        print("Query execution successful:", success)

    asyncio.run(execute_query())

**Insert Base64 Encoded Data**

Insert base64 encoded data into a database table.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager
    from DbUnify.SQLite3.aio.Raw import Raw

    async def insert_base64_data():
        manager = Manager(db_name='database.db')
        raw = Raw(manager)

        data_dict = {
            'name': 'max',
            'age': 24,
            'department': 'security'
        }

        await raw.insert_base64('employees', data_dict)
        print("Base64 data insertion complete")

    asyncio.run(insert_base64_data())

**List All Tables**

Get a list of all tables in the SQLite database.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager
    from DbUnify.SQLite3.aio.Raw import Raw

    async def list_tables():
        manager = Manager(db_name='database.db')
        raw = Raw(manager)
        tables = await raw.list_tables()
        print("Tables in database:", tables)

    asyncio.run(list_tables())

**Read Base64 Encoded Data**

Read and decode base64 encoded data from a database table.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.Manager import Manager
    from DbUnify.SQLite3.aio.Raw import Raw

    async def read_base64_data():
        manager = Manager(db_name='database.db')
        raw = Raw(manager)
        data = await raw.read_base64('employees', only_base64=True)
        print("Base64 data read from table:", data)

    asyncio.run(read_base64_data())
