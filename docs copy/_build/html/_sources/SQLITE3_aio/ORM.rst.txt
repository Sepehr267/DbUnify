ORM
===

This module includes the asynchronous ORM functionalities for the SQLite3 subpackage.

.. automodule:: DbUnify.SQLite3.aio.ORM.ORMManager
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: DbUnify.SQLite3.aio.ORM.Model
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: DbUnify.SQLite3.aio.ORM.Field
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: DbUnify.SQLite3.aio.ORM.ORMException
   :members:
   :undoc-members:
   :show-inheritance:

Examples
--------

**Field and Model Definition**

Define fields and models using the ORM functionalities.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.ORM import ORMManager, Model, Field, Field
    from DbUnify.SQLite3.data import *

    class User(Model):
        id = Field(data_type=DataType.INTEGER, constraints=[Rules.AUTOINCREMENT])
        name = Field(data_type=DataType.TEXT, constraints=[None])
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(db_name='example.db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        await orm_manager.close()

    asyncio.run(main())

**Fetch All Rows**

Fetch all rows from a table.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.ORM import ORMManager, Model, Field
    from DbUnify.SQLite3.data import *

    class User(Model):
        id = Field(data_type=DataType.INTEGER, constraints=[Rules.AUTOINCREMENT])
        name = Field(data_type=DataType.TEXT, constraints=[None])
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        async with ORMManager(db_name='example.db') as orm_manager:
            User.set_manager(orm_manager)
            await User.create_table()
            users = await User.fetch_all(query='SELECT * FROM user')
            print("All users:", users)

    asyncio.run(main())

**Create Table**

Create a table using the ORM functionalities.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.ORM import ORMManager, Model, Field
    from DbUnify.SQLite3.data import *

    class User(Model):
        id = Field(data_type=DataType.INTEGER, constraints=[Rules.AUTOINCREMENT])
        name = Field(data_type=DataType.TEXT, constraints=[None])
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(db_name='example.db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        await orm_manager.close()

    asyncio.run(main())

**Insert Row**

Insert a row into a table.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.ORM import ORMManager, Model, Field
    from DbUnify.SQLite3.data import *

    class User(Model):
        id = Field(data_type=DataType.INTEGER, constraints=[Rules.AUTOINCREMENT])
        name = Field(data_type=DataType.TEXT, constraints=[None])
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(db_name='example.db')
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
    from DbUnify.SQLite3.aio.ORM import ORMManager, Model, Field
    from DbUnify.SQLite3.data import *

    class User(Model):
        id = Field(data_type=DataType.INTEGER, constraints=[Rules.AUTOINCREMENT])
        name = Field(data_type=DataType.TEXT, constraints=[None])
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(db_name='example.db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        users = await User.select()
        print("Users:", users)
        await orm_manager.close()

    asyncio.run(main())

**Update Row**

Update a row in the table.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.ORM import ORMManager, Model, Field
    from DbUnify.SQLite3.data import *

    class User(Model):
        id = Field(data_type=DataType.INTEGER, constraints=[Rules.AUTOINCREMENT])
        name = Field(data_type=DataType.TEXT, constraints=[None])
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(db_name='example.db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        await User.update_row(
            values={'name': 'mohsen loerstani'},
            condition_column='email',
            condition_value='john@example.com')
        await orm_manager.close()

    asyncio.run(main())

**Delete Row**

Delete a row from the table.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.ORM import ORMManager, Model, Field
    from DbUnify.SQLite3.data import *

    class User(Model):
        id = Field(data_type=DataType.INTEGER, constraints=[Rules.AUTOINCREMENT])
        name = Field(data_type=DataType.TEXT, constraints=[None])
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(db_name='example.db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        await User.delete_row(condition_column='email', condition_value='john@example.com')
        await orm_manager.close()

    asyncio.run(main())

**Drop Table**

Drop a table from the database.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.ORM import ORMManager, Model, Field
    from DbUnify.SQLite3.data import *

    class User(Model):
        id = Field(data_type=DataType.INTEGER, constraints=[Rules.AUTOINCREMENT])
        name = Field(data_type=DataType.TEXT, constraints=[None])
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(db_name='example.db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.create_table()
        await User.drop_table()
        await orm_manager.close()

    asyncio.run(main())

**Map Model**

Map a model to a database table and create it if it doesn’t exist.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.ORM import ORMManager, Model, Field
    from DbUnify.SQLite3.data import *

    class User(Model):
        id = Field(data_type=DataType.INTEGER, constraints=[Rules.AUTOINCREMENT])
        name = Field(data_type=DataType.TEXT, constraints=[None])
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        async with ORMManager(db_name='example.db') as orm_manager:
            await orm_manager.map_model(User)

    asyncio.run(main())


**Add column**

Add column a row from the table.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.ORM import ORMManager, Model, Field
    from DbUnify.SQLite3.data import DataType

    class User(Model):
        id = Field(data_type=DataType.INTEGER, constraints=[Rules.AUTOINCREMENT])
        name = Field(data_type=DataType.TEXT, constraints=[None])
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(db_name='example.db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.add_column(column_name='address', data_type=DataType.TEXT)
        await orm_manager.close()

    asyncio.run(main())


**Delete column**

Delete column a row from the table.

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.ORM import ORMManager, Model, Field
    from DbUnify.SQLite3.data import DataType

    class User(Model):
        id = Field(data_type=DataType.INTEGER, constraints=[Rules.AUTOINCREMENT])
        name = Field(data_type=DataType.TEXT, constraints=[None])
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(db_name='example.db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        await User.delete_column(column_name='address')
        await orm_manager.close()

    asyncio.run(main())


**Alter table schema**

Alter table schema

.. code-block:: python

    import asyncio
    from DbUnify.SQLite3.aio.ORM import ORMManager, Model, Field
    from DbUnify.SQLite3.data import DataType

    class User(Model):
        id = Field(data_type=DataType.INTEGER, constraints=[Rules.AUTOINCREMENT])
        name = Field(data_type=DataType.TEXT, constraints=[None])
        email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

    async def main():
        orm_manager = ORMManager(db_name='example.db')
        await orm_manager.connect()
        User.set_manager(orm_manager)
        data = await User.alter_table_schema()
        print(data)
        await orm_manager.close()

    asyncio.run(main())
