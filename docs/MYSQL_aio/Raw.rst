Raw
===

This module handles raw database interactions in asynchronous contexts.

.. automodule:: DbUnify.MySQL.aio.Raw.Raw
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------------------

First, import the necessary modules and initialize the `Raw` class.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager
    from DbUnify.MySQL.aio.Raw import Raw

    async def main():
        manager = Manager(host='localhost', user='user', password='password', database='database')
        raw = Raw(manager)

    asyncio.run(main())

**Execute a SQL Query**

Execute a raw SQL query.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager
    from DbUnify.MySQL.aio.Raw import Raw

    async def execute_query():
        manager = Manager(host='localhost', user='user', password='password', database='database')
        raw = Raw(manager)
        success = await raw.execute_query("CREATE TABLE IF NOT EXISTS test (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
        print("Query execution successful:", success)

    asyncio.run(execute_query())


**Table List**

Get Table List

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.Manager import Manager
    from DbUnify.MySQL.aio.Raw import Raw

    async def execute_query():
        manager = Manager(host='localhost', user='user', password='password', database='database')
        raw = Raw(manager)
        success = await raw.list_tables()
        print("Table List:", success)

    asyncio.run(execute_query())


