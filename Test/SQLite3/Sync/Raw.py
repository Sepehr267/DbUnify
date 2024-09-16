from DbUnify.SQLite3.sync.Raw import Raw
from DbUnify.SQLite3.sync.Manager import Manager

# Initialize Manager and Raw
manager = Manager(db_name='example.db')
raw = Raw(manager=manager)

# # Backup the database
# success = raw.backup_database(backup_path='backups/example_backup.db')
# if success:
#     print("Backup successful")
# else:
#     print("Backup failed")

# Restore the database from a backup
# success = raw.restore_database(backup_path='backups/example_backup.db')
# if success:
#     print("Restore successful")
# else:
#     print("Restore failed")

# Execute a query to create a table
# success = raw.execute_query('CREATE TABLE IF NOT EXISTS user2 (id INTEGER PRIMARY KEY, name TEXT)')
# if success:
#     print("Table created successfully")
# else:
#     print("Failed to create table")

# # List tables in the database
# tables = raw.list_tables()
# print("Tables:", tables)

# data = {
#     'id': 253,  # Ensure this matches the expected integer type
#     'name': 'Sepehr'
# }

# try:
#     raw.insert_base64(table_name='user2', data_dict=data)
#     print("Data inserted successfully")
# except RuntimeError as e:
#     print(f"Error inserting data: {e}")

# Read base64 encoded data
# try:
#     rows = raw.read_base64(table_name='user2', only_base64=True)
#     for row in rows:
#         print("Decoded data:", row)
# except RuntimeError as e:
#     print(f"Error reading data: {e}")
