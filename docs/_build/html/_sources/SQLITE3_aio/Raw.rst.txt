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
