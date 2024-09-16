from DbUnify.SQLite3.sync import *
from DbUnify.SQLite3.data import *

manager = Manager(db_name='example.db', sql_injection_detection=False)

# Connect to the database
manager.connect()

# Create a new table
# manager.create_table(
#     table_name='users',
#     columns=[
#         ('id', DataType.INTEGER, [None]),
#         ('name', DataType.TEXT, [None]),
#         ('email', DataType.TEXT, [None])
#     ]
# )

# # Add a new column to an existing table
# manager.add_column(
#     table_name='users',
#     column_name='age',
#     data_type='INTEGER',
#     constraints='DEFAULT 18'
# )

# # Delete a column from an existing table
# manager.delete_column(
#     table_name='users',
#     column_name='age'
# )

# Insert a row into the table
# manager.insert_row(
#     table_name='users',
#     values={
#         'id': 2,
#         'name': "John Doe admin'or 1=1 or ''='",
#         'email': 'john.doe@example.com'
#         }
# )

# Get columns and data types for a table
# columns = manager.get_table_columns('users')

# # Print columns
# print(columns)

# results = manager.fetch_all('SELECT * FROM users')

# # Print results
# print(results)

# Delete a row from the table
# manager.delete_row(
#     table_name='users',
#     id=1
# )

# # Fetch all rows from the table
# rows = manager.select('users')

# # Print rows
# print(rows)

# Fetch a single row from the table
# row = manager.select_one(
#     table_name='users',
#     name = "John Doe admin'or 1=1 or ''='"
# )

# # Print row
# print(row)

# manager.update_row(
#     table_name='users',
#     values={
#         'name' : "Sepehr"
#     },
#     id = 2
# )

# manager.drop_table('users')

# Close the connection
manager.close()