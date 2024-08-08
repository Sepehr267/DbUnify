ORM
===

This module includes the synchronous ORM functionalities for the SQLite3 subpackage.

.. automodule:: DbUnify.SQLite3.sync.ORM.ORMManager
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: DbUnify.SQLite3.sync.ORM.Model
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: DbUnify.SQLite3.sync.ORM.Field
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: DbUnify.SQLite3.sync.ORM.ORMException
   :members:
   :undoc-members:
   :show-inheritance:
   
Examples
--------

**Field**

The `Field` class is used to define the fields in a model. You should use `Rules` and `DataType` for specifying data types and constraints.

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a field with data type and constraints
    field = Field(data_type=DataType.TEXT, constraints=[Rules.NOT_NULL])

**Model**

The `Model` class provides ORM functionalities for managing database models.

Before executing any ORM operations, ensure that the ORMManager instance is set.

**add_column**

Add a column to the table using the ORMManager instance:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Add a new column to the model's table
    User.add_column(column_name='age', data_type=DataType.INTEGER, constraints=[Rules.DEFAULT, '18'])

**alter_table_schema**

Apply schema changes to the database based on the model’s fields:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Apply schema changes
    User.alter_table_schema()

**apply_migrations**

Apply migrations to the database schema based on the model’s fields:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Apply migrations
    User.apply_migrations()

**create_table**

Create the table in the database using the ORMManager instance:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Create the table
    User.create_table()

**create_table_schema**

Generate the SQL schema for creating a table based on the model’s fields:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Generate table schema
    schema = User.create_table_schema()
    print(schema)

**delete_column**

Delete a column from the table using the ORMManager instance:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Delete a column from the table
    User.delete_column(column_name='age')

**delete_row**

Delete a row from the table based on a condition:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Delete a row with a specific condition
    User.delete_row(condition='email = ?', 'john.doe@example.com')

**drop_table**

Drop the table from the database:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Drop the table
    User.drop_table()

**fetch_all**

Execute a query and fetch all results:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Fetch all results for a query
    results = User.fetch_all('SELECT * FROM users')
    print(results)

**get_fields**

Get the fields of the model:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Get the model fields
    fields = User.get_fields()
    print(fields)

**get_orm_manager**

Get the ORMManager instance for the model:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Get ORM manager instance
    orm_manager_instance = User.get_orm_manager()
    print(orm_manager_instance)

**get_table_columns**

Get the columns and their data types for the table:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Get columns for the table
    columns = User.get_table_columns()
    print(columns)

**get_table_name**

Get the table name for the model:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Get the table name
    table_name = User.get_table_name()
    print(table_name)

**insert_row**

Insert a row into the table:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Insert a row into the table
    User.insert_row({
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })

**map_model**

Map the model to a database table and create it if it doesn’t exist:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Map the model to the database
    User.map_model()

**select**

Search for all rows in the table:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Fetch all rows from the table
    rows = User.select()
    print(rows)

**select_one**

Search for a single row based on a condition:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Fetch a single row based on a condition
    row = User.select_one(condition='email = ?', 'john.doe@example.com')
    print(row)

**set_manager**

Set the ORMManager instance for the model:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance
    orm_manager = ORMManager(db_name='example.db')

    # Set the ORMManager instance for the model
    User.set_manager(orm_manager)

**update_row**

Update a row in the table based on a condition:

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db')
    User.set_manager(orm_manager)

    # Update a row in the table
    User.update_row(
        values={'name': 'Jane Doe'},
        condition='email = ?',
        'john.doe@example.com'
    )