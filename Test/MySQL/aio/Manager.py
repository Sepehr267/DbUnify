from DbUnify.MySQL.aio import *
import asyncio

manager = Manager(
    host='localhost',
    user='root',
    password='',
    database='example_db',
    port=3306
)

# async def main():
#     await manager.connect()
    # await manager.create_table(
    # table_name='users',
    # columns=[
    #     ('id', 'INT', ['PRIMARY KEY', 'AUTO_INCREMENT']),
    #     ('name', 'VARCHAR(100)', ['NOT NULL']),
    #     ('email', 'VARCHAR(100)', ['UNIQUE'])
    # ]
    # )

#     await manager.close()

# async def main():
#     await manager.connect()
#     await manager.add_column(
#         table_name='users',
#         column_name='age',
#         data_type=DataType.VARCHAR(255),
#         constraints=Rules.NOT_NULL)
#     print("Column added")

#     await manager.close()


# async def main():
#     await manager.connect()
#     await manager.delete_column('users', 'age')
#     print("Column Deleted")
#     await manager.close()

# async def main():
#     await manager.connect()
#     await manager.insert_row(
#         table_name='users',
#         values={
#             'name': 'John Doe',
#             'email': 'JohnDoe@gmail.com'
#             }
#     )
#     print("Row added")

#     await manager.close()

# async def main():
#     await manager.connect()
    # await manager.update_row(
    #     table_name='users',
    #     values={'email': 'JoneDoe@yahoo.com'},
    #     condition='name = John Doe'
    # )
#     print("Row deleted")

#     await manager.close()


# async def main():
#     await manager.connect()
#     data = await manager.select('users')
#     print(data)

#     await manager.close()

# async def main():
#     await manager.connect()
#     data = await manager.select_one('users', condition='name = John Doe')
#     print(data)

#     await manager.close()

# async def main():
#     await manager.connect()
#     await manager.drop_table('users')
#     print('Table Droped')

#     await manager.close()

asyncio.run(main())