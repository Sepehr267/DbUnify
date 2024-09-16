import asyncio
from DbUnify.SQLite3.aio.ORM import ORMManager, Model
from DbUnify.SQLite3.aio.ORM.Types import IntegerField, TextField
from DbUnify.SQLite3.data import *

class User(Model):
    id = IntegerField(constraints=[Rules.PRIMARY_KEY])
    name = TextField(constraints=[Rules.NOT_NULL])
    email = TextField(constraints=[Rules.UNIQUE])

# async def main():
#     orm_manager = ORMManager(db_name='example.db')
#     await orm_manager.connect()
#     User.set_manager(orm_manager)
#     await User.create_table()
#     await orm_manager.close()

# async def main():
#     orm_manager = ORMManager(db_name='example.db')
#     await orm_manager.connect()
#     User.set_manager(orm_manager)
#     await User.create_table()
#     await User.insert_row(values={'name': 'John Doe', 'email': 'john@example.com'})
#     await orm_manager.close()

# async def main():
#     orm_manager = ORMManager(db_name='example.db')
#     await orm_manager.connect()
#     User.set_manager(orm_manager)
#     users = await User.select()
#     print("Users:", users)
#     await orm_manager.close()

# async def main():
#     orm_manager = ORMManager(db_name='example.db')
#     await orm_manager.connect()
#     User.set_manager(orm_manager)
#     await User.update_row(values={'name': 'mohsen loerstani'}, condition_column='email', condition_value='john@example.com')
#     await orm_manager.close()

# async def main():
#     orm_manager = ORMManager(db_name='example.db')
#     await orm_manager.connect()
#     User.set_manager(orm_manager)
#     await User.delete_row(condition_column='email', condition_value='john@example.com')
#     await orm_manager.close()

# async def main():
#     async with ORMManager(db_name='example.db') as orm_manager:
#         User.set_manager(orm_manager)
#         await orm_manager.apply_migrations(User)

# async def main():
#     async with ORMManager(db_name='example.db') as orm_manager:
#         await orm_manager.map_model(User)

# async def main():
#     orm_manager = ORMManager(db_name='example.db')
#     await orm_manager.connect()
#     User.set_manager(orm_manager)
#     await User.add_column(column_name='address', data_type=DataType.TEXT)
#     await orm_manager.close()

# async def main():
#     orm_manager = ORMManager(db_name='example.db')
#     await orm_manager.connect()
#     User.set_manager(orm_manager)
#     await User.delete_column(column_name='address')
#     await orm_manager.close()

# async def main():
#     orm_manager = ORMManager(db_name='example.db')
#     await orm_manager.connect()
#     User.set_manager(orm_manager)
#     data = await User.alter_table_schema()
#     await orm_manager.close()

asyncio.run(main())