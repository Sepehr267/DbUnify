Raw
===

This module handles raw database interactions in asynchronous contexts.

.. automodule:: DbUnify.MySQL.sync.Raw.Raw
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------------------

First, import the necessary modules and initialize the `Raw` class.

.. code-block:: python

    from DbUnify.MySQL.sync.Manager import Manager
    from DbUnify.MySQL.sync.Raw import Raw

    manager = Manager(host='localhost', user='user', password='password', database='database')
    raw = Raw(manager)

**Execute a SQL Query**

Execute a raw SQL query.

.. code-block:: python

    from DbUnify.MySQL.sync.Manager import Manager
    from DbUnify.MySQL.sync.Raw import Raw

    manager = Manager(host='localhost', user='user', password='password', database='database')
    raw = Raw(manager)
    success = raw.execute_query("CREATE TABLE IF NOT EXISTS test (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    print("Query execution successful:", success)


**List Tables**

Get Table List

.. code-block:: python

    from DbUnify.MySQL.sync.Manager import Manager
    from DbUnify.MySQL.sync.Raw import Raw

    manager = Manager(host='localhost', user='user', password='password', database='database')
    raw = Raw(manager)
    data = raw.list_tables()
    print(data)
