ORM
===

This module includes the synchronous ORM functionalities for the MySQL subpackage.

.. automodule:: DbUnify.MySQL.sync.ORM.ORMManager
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: DbUnify.MySQL.sync.ORM.Model
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: DbUnify.MySQL.sync.ORM.Field
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: DbUnify.MySQL.sync.ORM.ORMException
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------

**Field and Model Definition**

Define fields and models using the ORM functionalities.

.. code-block:: python

    from DbUnify.MySQL.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        
        User.set_manager(orm_manager)
        User.create_table()
        

    main()

**Create Table**

Create a table using the ORM functionalities.

.. code-block:: python

    from DbUnify.MySQL.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        
        User.set_manager(orm_manager)
        User.create_table()
        

    main()

**Insert Row**

Insert a row into a table.

.. code-block:: python

    from DbUnify.MySQL.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        
        User.set_manager(orm_manager)
        User.create_table()
        User.insert_row(values={'name': 'John Doe', 'email': 'john@example.com'})
        

    main()

**Select Rows**

Select rows from a table.

.. code-block:: python

    from DbUnify.MySQL.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        
        User.set_manager(orm_manager)
        User.create_table()
        data = User.Select()
        print(data)

    main()

**Select one row**

Select one row from a table.

.. code-block:: python

    from DbUnify.MySQL.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        
        User.set_manager(orm_manager)
        user = User.select_one(name='John Doe')

    main()

**Update Row**

Update a row in the table.

.. code-block:: python

    from DbUnify.MySQL.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        
        User.set_manager(orm_manager)
        User.create_table()
        User.update_row(
            condition='name = John Doe',
            values={
                    'email' : 'john@newdomain.com'
                })

    main()

**Delete Row**

Delete a row from the table.

.. code-block:: python

    from DbUnify.MySQL.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        
        User.set_manager(orm_manager)
        User.create_table()
        User.delete_row(name='John Doe')
        
    main()

**Drop Table**

Drop a table from the database.

.. code-block:: python

    from DbUnify.MySQL.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        
        User.set_manager(orm_manager)
        User.create_table()
        User.drop_table()

    main()

