Manager
========

This module is responsible for managing synchronous database operations.

.. automodule:: DbUnify.SQLite3.sync.Manager.Manager
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------

**add_column**

Add a column to an existing table:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(db_name='example.db')

    # Connect to the database
    manager.connect()

    # Add a new column to an existing table
    manager.add_column(
        table_name='users',
        column_name='age',
        data_type='INTEGER',
        constraints='DEFAULT 18'
    )

    # Close the connection
    manager.close()

**close**

Close the database connection:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(db_name='example.db')

    # Connect to the database
    manager.connect()

    # Perform some database operations...

    # Close the database connection
    manager.close()

**connect**

Connect to the SQLite database:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(db_name='example.db')

    # Connect to the SQLite database
    manager.connect()

**create_table**

Create a new table:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(db_name='example.db')

    # Connect to the database
    manager.connect()

    # Create a new table
    manager.create_table(
        table_name='users',
        columns=[
            ('id', 'INTEGER', ['PRIMARY KEY', 'AUTOINCREMENT']),
            ('name', 'TEXT', ['NOT NULL']),
            ('email', 'TEXT', ['UNIQUE'])
        ]
    )

    # Close the connection
    manager.close()

**delete_column**

Delete a column from an existing table:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(db_name='example.db')

    # Connect to the database
    manager.connect()

    # Delete a column from an existing table
    manager.delete_column(
        table_name='users',
        column_name='age'
    )

    # Close the connection
    manager.close()

**delete_row**

Delete a row based on a condition:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(db_name='example.db')

    # Connect to the database
    manager.connect()

    # Delete a row from the table
    manager.delete_row(
        table_name='users',
        condition='id = ?',
        1
    )

    # Close the connection
    manager.close()

**drop_table**

Drop a table from the database:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(db_name='example.db')

    # Connect to the database
    manager.connect()

    # Drop a table from the database
    manager.drop_table('users')

    # Close the connection
    manager.close()

**fetch_all**

Execute a query and fetch all results:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(db_name='example.db')

    # Connect to the database
    manager.connect()

    # Fetch all results for a query
    results = manager.fetch_all('SELECT * FROM users')

    # Print results
    print(results)

    # Close the connection
    manager.close()

**get_table_columns**

Get the columns and their data types for a table:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(db_name='example.db')

    # Connect to the database
    manager.connect()

    # Get columns and data types for a table
    columns = manager.get_table_columns('users')

    # Print columns
    print(columns)

    # Close the connection
    manager.close()

**insert_row**

Insert a row into the table:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(db_name='example.db')

    # Connect to the database
    manager.connect()

    # Insert a row into the table
    manager.insert_row(
        table_name='users',
        values={
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        }
    )

    # Close the connection
    manager.close()

**select**

Search for all rows in the table:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(db_name='example.db')

    # Connect to the database
    manager.connect()

    # Fetch all rows from the table
    rows = manager.select('users')

    # Print rows
    print(rows)

    # Close the connection
    manager.close()

**select_one**

Search for a single row based on a condition:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(db_name='example.db')

    # Connect to the database
    manager.connect()

    # Fetch a single row from the table
    row = manager.select_one(
        table_name='users',
        condition='email = ?',
        'john.doe@example.com'
    )

    # Print row
    print(row)

    # Close the connection
    manager.close()

**update_row**

Update a row in the table based on a condition:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(db_name='example.db')

    # Connect to the database
    manager.connect()

    # Update a row in the table
    manager.update_row(
        table_name='users',
        values={
            'name': 'Jane Doe'
        },
        condition='email = ?',
        'john.doe@example.com'
    )

    # Close the connection
    manager.close()
