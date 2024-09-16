from DbUnify.MySQL.sync import *

manager = Manager(
    host='localhost',
    user='root',
    password='',
    database='example_db',
    port=3306
)
raw = Raw(manager)

# success = raw.execute_query("CREATE TABLE IF NOT EXISTS test (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
# print("Query execution successful:", success)

# List table
# data = raw.list_tables()
# print(data)