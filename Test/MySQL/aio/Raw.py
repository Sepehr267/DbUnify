import asyncio
from DbUnify.MySQL.aio import Manager, Raw

manager = Manager(
        host='localhost',
        user='root',
        password='',
        database='example_db',
        port=3306
    )

raw = Raw(manager)
    

async def main():
    await manager.connect()
    # success = await raw.execute_query("CREATE TABLE IF NOT EXISTS test (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
    # print("Query execution successful:", success)

    # data = await raw.list_tables()
    # print(data)
    await manager.close()

if __name__ == "__main__":
    asyncio.run(main())
