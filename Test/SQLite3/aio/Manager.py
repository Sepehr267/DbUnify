import asyncio
from DbUnify.SQLite3.aio.Manager import Manager
from DbUnify.SQLite3.data import DataType, Rules

# async def main():
#     manager = Manager(db_name='example.db')
#     await manager.connect()  # Correct method name for connecting
#     print("Connected to the database")

# async def main():
#     manager = Manager(db_name='example.db')
#     await manager.connect()
    # await manager.create_table(
    #     table_name='users',
    #     columns=[
    #         ('id', DataType.INTEGER, [Rules.PRIMARY_KEY]),
    #         ('name', DataType.TEXT, [Rules.NOT_NULL]),
    #     ]
    # )
#     print("Table created")
#     await manager.close()

# async def main():
#     manager = Manager(db_name='example.db')
#     await manager.connect()
#     await manager.drop_table('users')
#     print("Table dropped")
#     await manager.close()

# async def main():
#     manager = Manager(db_name='example.db')
#     await manager.connect()
    # await manager.add_column(
    #     table_name='users',
    #     column_name='email',
    #     data_type=DataType.TEXT
    # )
#     print("Column added")
#     await manager.close()

# async def main():
#     manager = Manager(db_name='example.db')
#     await manager.connect()
#     await manager.delete_column('users', 'email')
#     print("Column deleted")
#     await manager.close()

# async def main():
#     manager = Manager(db_name='example.db')
#     await manager.connect()
    # await manager.insert_row(
    #     table_name='users',
    #     values={
    #         'id': 1,
    #         'name': 'John Doe'
    #     }
    # )
#     print("Row inserted")
#     await manager.close()

# async def main():
#     manager = Manager(db_name='example.db')
#     await manager.connect()
    # await manager.delete_row(
    #     table_name='users',
    #     condition_column='name',
    #     condition_value='John Doe'
    # )
#     print("Row deleted")
#     await manager.close()

# async def main():
#     manager = Manager(db_name='example.db')
#     await manager.connect()
    # await manager.update_row(
    #     table_name='users',
    #     values={'email': 'Jane Doe@gmail.com'},  # Note the corrected email domain
    #     condition_column='name',
    #     condition_value='John Doe'
    # )
#     print("Row updated")
#     await manager.close()

# async def main():
#     manager = Manager(db_name='example.db')
#     await manager.connect()
#     rows = await manager.select('users')
#     print("Rows selected:", rows)

# async def main():
#     manager = Manager(db_name='example.db')
#     await manager.connect()
    # row = await manager.select_one(
    #     table_name='users',
    #     name='John Doe'
    # )
#     print("Row selected:", row)

# async def main():
#     manager = Manager(db_name='example.db')
#     await manager.connect()
#     columns = await manager.get_table_columns('users')
#     print("Table columns:", columns)

asyncio.run(main())
