Manager
========

This module is responsible for managing synchronous database operations.

.. automodule:: DbUnify.SQLite3.sync.Manager.Manager
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------

**Connecting to the Database**


.. code-block:: python

    from DbUnify.SQLite3.sync import Manager
    
    manager = Manager(db_name='example.db')

    manager.connect()


**Create Table**


.. code-block:: python

    from DbUnify.SQLite3.sync import Manager
    from DbUnify.SQLite3.data import *
    
    manager = Manager(db_name='example.db')

    manager.connect()

    manager.create_table(
        table_name='users',
        columns=[
            ('id', DataType.INTEGER, [None]),
            ('name', DataType.TEXT, [None]),
            ('email', DataType.TEXT, [None])
    ])


**Add a new column**


.. code-block:: python

    from DbUnify.SQLite3.sync import Manager
    
    manager = Manager(db_name='example.db')

    manager.connect()

    # NOTE: add_column not Support DataType and Rules
    
    manager.add_column(
        table_name='users',
        column_name='age',
        data_type='INTEGER',
        constraints='DEFAULT 18'
    )


**Delete a column**


.. code-block:: python

    from DbUnify.SQLite3.sync import Manager
    
    manager = Manager(db_name='example.db')

    manager.connect()

    
    manager.delete_column(
        table_name='users',
        column_name='age'
        )


**Insert a row**


.. code-block:: python

    from DbUnify.SQLite3.sync import Manager
    
    manager = Manager(db_name='example.db')

    manager.connect()

    
    manager.insert_row(
    table_name='users',
    values={
        'id': 2,
        'name': "John Doe",
        'email': 'john.doe@example.com'
        })


**Get columns**


.. code-block:: python

    from DbUnify.SQLite3.sync import Manager
    
    manager = Manager(db_name='example.db')

    manager.connect()

    columns = manager.get_table_columns('users')
    print(columns)


**Delete a row**


.. code-block:: python

    from DbUnify.SQLite3.sync import Manager
    
    manager = Manager(db_name='example.db')

    manager.connect()

    manager.delete_row(
        table_name='users',
        id=1
        )


**Select all rows*


.. code-block:: python

    from DbUnify.SQLite3.sync import Manager
    
    manager = Manager(db_name='example.db')

    manager.connect()

    rows = manager.select('users')
    print(rows)


**Update row*


.. code-block:: python

    from DbUnify.SQLite3.sync import Manager
    
    manager = Manager(db_name='example.db')

    manager.connect()

    manager.update_row(
        table_name='users',
        values={
            'name' : "Sepehr"
        },
        id = 2)


**Drop Table*


.. code-block:: python

    from DbUnify.SQLite3.sync import Manager
    
    manager = Manager(db_name='example.db')

    manager.connect()

    manager.drop_table('users')


**Close the connecting*


.. code-block:: python

    from DbUnify.SQLite3.sync import Manager
    
    manager = Manager(db_name='example.db')

    manager.connect()

    manager.close()