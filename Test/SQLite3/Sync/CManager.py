from DbUnify.SQLite3.sync.CManager import CManager
from DbUnify.SQLite3.sync import CMCoreBuilder, get_core 

builder = CMCoreBuilder()
builder.build_core()

# Connect to the database
# db = CManager("Lab/Manager.dll") windows
print(get_core())
db = CManager(get_core()) # Linux

db.connect_db('database.db')
# Create a table
db.create_table(
    "users",
    [
        ('id', 'INTEGER', ['NOT NULL', 'PRIMARY KEY']),
        ('name', 'TEXT', ['NOT NULL']),
        ('email', 'TEXT', ['UNIQUE'])
    ]
)

# Insert a row
db.insert_row("users", {
    'name': 'John Doe',
    'email': "john.doe@example.com"
})
print("Row inserted.")



# Update the row
db.update_row("users", {'email': 'john.doe@newdomain.com'}, "name = 'John Doe'")
print("Row updated.")

data = db.fetch_all('select * from users')
print(data)

# Delete the row
# db.delete_row("users", "name = 'John Doe'")
# print("Row deleted.")

# # # Drop the table
# db.drop_table("users")
# print("Table dropped.")
