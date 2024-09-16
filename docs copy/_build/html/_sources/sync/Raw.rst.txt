
Raw
---------

**Raw** provides methods for executing raw SQL queries, creating and restoring database backups, listing tables, and handling base64 encoded data.

.. autoclass:: DbUnify.SQLite3.sync.Raw.Raw
   :members:
   :undoc-members:
   :show-inheritance:

**Attributes:**

- `manager (Manager)`: The Manager instance managing the database connection.

**Methods:**

**__init__**

Initialize the Raw instance with a Manager instance.

.. code-block:: python

    from DbUnify.SQLite3.sync.Raw import Raw
    from DbUnify.SQLite3.sync.Manager import Manager

    # Initialize Manager and Raw
    manager = Manager(db_name='example.db')
    raw = Raw(manager=manager)

**backup_database**

Create a backup of the database.

.. code-block:: python

    from DbUnify.SQLite3.sync.Raw import Raw
    from DbUnify.SQLite3.sync.Manager import Manager

    # Initialize Manager and Raw
    manager = Manager(db_name='example.db')
    raw = Raw(manager=manager)

    # Backup the database
    success = raw.backup_database(backup_path='backups/example_backup.db')
    if success:
        print("Backup successful")
    else:
        print("Backup failed")

**restore_database**

Restore the database from a backup.

.. code-block:: python

    from DbUnify.SQLite3.sync.Raw import Raw
    from DbUnify.SQLite3.sync.Manager import Manager

    # Initialize Manager and Raw
    manager = Manager(db_name='example.db')
    raw = Raw(manager=manager)

    # Restore the database from a backup
    success = raw.restore_database(backup_path='backups/example_backup.db')
    if success:
        print("Restore successful")
    else:
        print("Restore failed")

**execute_query**

Execute a database query.

.. code-block:: python

    from DbUnify.SQLite3.sync.Raw import Raw
    from DbUnify.SQLite3.sync.Manager import Manager

    # Initialize Manager and Raw
    manager = Manager(db_name='example.db')
    raw = Raw(manager=manager)

    # Execute a query to create a table
    success = raw.execute_query('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    if success:
        print("Table created successfully")
    else:
        print("Failed to create table")

**list_tables**

Get a list of all tables in the SQLite database.

.. code-block:: python

    from DbUnify.SQLite3.sync.Raw import Raw
    from DbUnify.SQLite3.sync.Manager import Manager

    # Initialize Manager and Raw
    manager = Manager(db_name='example.db')
    raw = Raw(manager=manager)

    # List tables in the database
    tables = raw.list_tables()
    print("Tables:", tables)

**insert_base64**

Insert base64 encoded data into a database table.

.. code-block:: python

    from DbUnify.SQLite3.sync.Raw import Raw
    from DbUnify.SQLite3.sync.Manager import Manager

    # Initialize Manager and Raw
    manager = Manager(db_name='example.db')
    raw = Raw(manager=manager)

    # Data to be inserted
    data = {
        'file_data': 'some binary data',
    }

    # Insert base64 encoded data
    try:
        raw.insert_base64(table_name='files', data_dict=data)
        print("Data inserted successfully")
    except RuntimeError as e:
        print(f"Error inserting data: {e}")

**read_base64**

Read and decode base64 encoded data from a database table.

.. code-block:: python

    from DbUnify.SQLite3.sync.Raw import Raw
    from DbUnify.SQLite3.sync.Manager import Manager

    # Initialize Manager and Raw
    manager = Manager(db_name='example.db')
    raw = Raw(manager=manager)

    # Read base64 encoded data
    try:
        rows = raw.read_base64(table_name='files', only_base64=True)
        for row in rows:
            print("Decoded data:", row)
    except RuntimeError as e:
        print(f"Error reading data: {e}")

