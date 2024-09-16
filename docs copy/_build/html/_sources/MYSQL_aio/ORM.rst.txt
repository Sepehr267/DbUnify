ORM
===

This module includes the asynchronous ORM functionalities for the MySQL subpackage.

.. automodule:: DbUnify.MySQL.aio.ORM.ORMManager
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: DbUnify.MySQL.aio.ORM.Model
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: DbUnify.MySQL.aio.ORM.Field
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: DbUnify.MySQL.aio.ORM.ORMException
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------

**Field and Model Definition**

Define fields and models using the ORM functionalities.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        await orm_manager.close()

    asyncio.run(main())

**Create Table**

Create a table using the ORM functionalities.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        await orm_manager.close()

    asyncio.run(main())


**Add Column**

Add a Column to table using the ORM functionalities.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.add_column(
            column_name='age',
            data_type=DataType.VARCHAR(255),
            constraints=Rules.NOT_NULL
        )
        await orm_manager.close()

    asyncio.run(main())


**Delete Column**

Delete a Column to table using the ORM functionalities.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.delete_column('age')
        await orm_manager.close()

    asyncio.run(main())

**Insert Row**

Insert a row into a table.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        await User.insert_row(values={'name': 'John Doe', 'email': 'john@example.com'})
        await orm_manager.close()

    asyncio.run(main())

**Select Rows**

Select rows from a table.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        users = await User.select()
        print("Users:", users)
        await orm_manager.close()

    asyncio.run(main())

**Select one row**

Select one row from a table.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        user = await User.select_one(name='John Doe')
        print("Users:", users)
        await orm_manager.close()

    asyncio.run(main())

**Update Row**

Update a row in the table.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        await User.update_row(condition='name = "John Doe"', age='30')
        await orm_manager.close()

    asyncio.run(main())

**Delete Row**

Delete a row from the table.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        await User.delete_row(name='John Doe')
        await orm_manager.close()

    asyncio.run(main())

**Drop Table**

Drop a table from the database.

.. code-block:: python

    import asyncio
    from DbUnify.MySQL.aio.ORM import ORMManager, Model, Field
    from DbUnify.MySQL.data import Rules, DataType

    class User(Model):
        id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTOINCREMENT])
        name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
        email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(host='localhost', user='user', password='password', database='example_db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        await User.drop_table()
        await orm_manager.close()

    asyncio.run(main())

