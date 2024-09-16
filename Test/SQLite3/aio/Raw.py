import asyncio
from DbUnify.SQLite3.aio.Manager import Manager
from DbUnify.SQLite3.aio.Raw import Raw

manager = Manager(db_name='example.db')
raw = Raw(manager)

# async def main():
#     success = await raw.backup_database('backup.db')
#     print("Backup successful:", success)

# async def main():
#     success = await raw.restore_database('backup.db')
#     print("Restore successful:", success)

# async def main():
#     await manager.connect()
#     success = await raw.execute_query("CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)")
#     print("Query execution successful:", success)
#     await manager.close()

asyncio.run(main())
