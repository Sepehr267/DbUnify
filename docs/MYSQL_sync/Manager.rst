Manager
========

The `Manager` class provides an interface for managing MySQL databases asynchronously. It offers methods for connecting to the database, executing SQL queries, creating and modifying tables, inserting and deleting rows, and closing the database connection.

Module
-------

.. automodule:: DbUnify.MySQL.sync.Manager
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------

**Connecting to the database**

Connect to the MySQL database:

.. code-block:: python

    from DbUnify.MySQL.sync import Manager

    # Create an instance of the Manager class
    manager = Manager(
        host='localhost',
        user='root',
        password='password',
        database='example_db',
        port=3306
    )

    # Connect to the MySQL database
    manager.connect()

**Creating a table**

Create a new table:

.. code-block:: python

    from DbUnify.MySQL.sync import Manager

    # Create an instance of the Manager class
    manager = Manager(
        host='localhost',
        user='root',
        password='password',
        database='example_db',
        port=3306
    )

    # Connect to the database
    manager.connect()

    # Create a new table
    manager.create_table(
        table_name='users',
        columns=[
            ('id', 'INT', ['PRIMARY KEY', 'AUTO_INCREMENT']),
            ('name', 'VARCHAR(100)', ['NOT NULL']),
            ('email', 'VARCHAR(100)', ['UNIQUE'])
        ]
    )

    # Close the connection
    manager.close()

**Inserting a row**

Insert a row into a table:

.. code-block:: python

    from DbUnify.MySQL.sync import Manager

    # Create an instance of the Manager class
    manager = Manager(
        host='localhost',
        user='root',
        password='password',
        database='example_db',
        port=3306
    )

    # Connect to the database
    manager.connect()

    # Insert a row into the users table
    manager.insert_row(
        table_name='users',
        values={
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        }
    )

    # Close the connection
    manager.close()

**Updating a row**

Update a row in a table:

.. code-block:: python

    from DbUnify.MySQL.sync import Manager

    # Create an instance of the Manager class
    manager = Manager(
        host='localhost',
        user='root',
        password='password',
        database='example_db',
        port=3306
    )

    # Connect to the database
    manager.connect()

    # Update a row in the users table
    manager.update_row(
        table_name='users',
        values={
            'email': 'john.new@example.com'
        },
        condition='name = "John Doe"'
    )

    # Close the connection
    manager.close()

**Deleting a row**

Delete a row from a table:

.. code-block:: python
    
    from DbUnify.MySQL.sync import Manager

    # Create an instance of the Manager class
    manager = Manager(
        host='localhost',
        user='root',
        password='password',
        database='example_db',
        port=3306
    )

    # Connect to the database
    manager.connect()

    # Delete a row from the users table
    manager.delete_row(
        table_name='users',
        condition='name = "John Doe"'
    )

    # Close the connection
    manager.close()

**Fetching all rows**

Fetch all rows from a table:

.. code-block:: python

    from DbUnify.MySQL.sync import Manager

    # Create an instance of the Manager class
    manager = Manager(
        host='localhost',
        user='root',
        password='password',
        database='example_db',
        port=3306
    )

    # Connect to the database
    manager.connect()

    # Fetch all rows from the users table
    rows = manager.fetch_all('SELECT * FROM users')
    print(rows)

    # Close the connection
    manager.close()

**Selecting one row**

Select a single row from a table:

.. code-block:: python

    from DbUnify.MySQL.sync import Manager

    # Create an instance of the Manager class
    manager = Manager(
        host='localhost',
        user='root',
        password='password',
        database='example_db',
        port=3306
    )

    # Connect to the database
    manager.connect()

    # Select a single row from the users table
    row = manager.select_one(
        table_name='users',
        condition='email = "john.new@example.com"'
    )
    print(row)

    # Close the connection
    manager.close()

**Dropping a table**

Drop a table from the database:

.. code-block:: python

    from DbUnify.MySQL.sync import Manager

    # Create an instance of the Manager class
    manager = Manager(
        host='localhost',
        user='root',
        password='password',
        database='example_db',
        port=3306
    )

    # Connect to the database
    manager.connect()

    # Drop the users table
    manager.drop_table('users')

    # Close the connection
    manager.close()

**Adding a column**

Add a column to an existing table:

.. code-block:: python

    from DbUnify.MySQL.sync import Manager

    # Create an instance of the Manager class
    manager = Manager(
        host='localhost',
        user='root',
        password='password',
        database='example_db',
        port=3306
    )

    # Connect to the database
    manager.connect()

    # Add a column to the users table
    # NOTE: add_column not Support Rules and DataType
    manager.add_column(
        table_name='users',
        column_name='age',
        data_type='INT',
        constraints='NULL'
    )

    # Close the connection
    manager.close()

**Deleting a column**

Delete a column from a table:

.. code-block:: python

    from DbUnify.MySQL.sync import Manager

    # Create an instance of the Manager class
    manager = Manager(
        host='localhost',
        user='root',
        password='password',
        database='example_db',
        port=3306
    )

    # Connect to the database
    manager.connect()

    # Delete a column from the users table
    manager.delete_column(
        table_name='users',
        column_name='age'
    )

    # Close the connection
    manager.close()

**Closing the connection**

Close the database connection:

.. code-block:: python

    # Create an instance of the Manager class
    manager = Manager(
        host='localhost',
        user='root',
        password='password',
        database='example_db',
        port=3306
    )

    # Connect to the MySQL database
    manager.connect()

    # Close the connection
    manager.close()
