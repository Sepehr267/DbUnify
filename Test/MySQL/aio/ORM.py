from DbUnify.MySQL.aio import *
import asyncio


orm_manager = ORMManager(host='localhost',
    user='root',
    password='',
    database='example_db',
    port=3306)

class User(Model):
    id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTO_INCREMENT])
    name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
    email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])

User.set_manager(orm_manager)

# async def main():
#     await orm_manager.connect()
#     await User.create_table()
#     await orm_manager.close()
#     print('table created')

# async def main():
#     await orm_manager.connect()
#     await User.insert_row(values={'name': 'John Doe', 'email': 'john@example.com'})
#     await orm_manager.close()
#     print('data inserted')

# async def main():
#     await orm_manager.connect()
#     users = await User.select()
#     print("Users:", users)
#     await orm_manager.close()

# async def main():
#     await orm_manager.connect()
#     user = await User.select_one(name='John Doe')
#     print("Users:", user)
#     await orm_manager.close()

# async def main():
#     await orm_manager.connect()
#     await User.update_row(condition='name = "John Doe"', age='30')
#     await orm_manager.close()
#     print('Row updated')

# async def main():
#     await orm_manager.connect()
#     await User.delete_row(name='John Doe')
#     await orm_manager.close()
#     print('Row Deleted')

# async def main():
#     await orm_manager.connect()
    # await User.add_column(
    #     column_name='age',
    #     data_type=DataType.VARCHAR(255),
    #     constraints=Rules.NOT_NULL
    # )
#     await orm_manager.close()
#     print('Column added')

# async def main():
#     await orm_manager.connect()
#     await User.delete_column('age')
#     await orm_manager.close()
#     print('Column deleted')

asyncio.run(main())