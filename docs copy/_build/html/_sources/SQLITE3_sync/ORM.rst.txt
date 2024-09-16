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
.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    # Define a model
    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    # Create an ORMManager instance and set it for the model
    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)


**Create Table**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    User.create_table()


**Add a new column**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    User.add_column(
        column_name='age',
        data_type=DataType.INTEGER,
        constraints=[Rules.NOT_NULL])


**Delete a column**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    User.delete_column(column_name='age')


**Apply schema changes**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    User.alter_table_schema()


**Apply migrations**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    User.apply_migrations()


**Generate table schema**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    schema = User.create_table_schema()
    print(schema)


**Generate table schema**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    schema = User.create_table_schema()
    print(schema)


**Insert a Row**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    User.insert_row({
        'name': 'Sepehr',
        'email': 'Sepehr@example.com'
        })


**Delete a row**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    User.delete_row('email = ?', 'Sepehr@yahoo.com')


**Fetch all**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    results = User.fetch_all('SELECT * FROM user')
    print(results)


**Select all rows**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    rows = User.select()
    print(rows)


**Select one rows**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    row = User.select_one('email = ?', 'Sepehr@example.com')
    print(row)


**Update a row**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    User.update_row(
        condition= 'name = Sepehr',
        values={'email': 'Sepehr@yahoo.com'},
    )


**Map the model to the database**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    User.map_model()


**Get the table name**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    table_name = User.get_table_name()
    print(table_name)


**Get columns**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    columns = User.get_table_columns()
    print(columns)


**Get ORM Manager instracne**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    orm_manager_instance = User.get_orm_manager()
    print(orm_manager_instance)


**Get the model fields**

.. code-block:: python

    from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
    from DbUnify.SQLite3.data import Rules, DataType

    class User(Model):
        name = Field(data_type=DataType.TEXT)
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
    User.set_manager(orm_manager)

    fields = User.get_fields()
    print(fields)

