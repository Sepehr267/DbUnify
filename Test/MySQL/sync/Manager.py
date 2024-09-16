from DbUnify.MySQL.sync import Manager

manager = Manager(
    host='localhost',
    user='root',
    password='',
    database='example_db',
    port=3306
)

# Connect to the MySQL database
# manager.connect()

# Create a new table
# manager.create_table(
#     table_name='users',
#     columns=[
#         ('id', 'INT', ['PRIMARY KEY', 'AUTO_INCREMENT']),
#         ('name', 'VARCHAR(100)', ['NOT NULL']),
#         ('email', 'VARCHAR(100)', ['UNIQUE'])
#     ]
# )

# Insert a row into the users table
# manager.insert_row(
#     table_name='users',
#     values={
#         'name': 'John Doe',
#         'email': 'john.doe@example.com'
#     }
# )

# Update a row in the users table
# manager.update_row(
#     table_name='users',
#     values={
#         'email': 'john.new@example.com'
#     },
#     condition='name = "John Doe"'
# )

# Delete a row from the users table
# manager.delete_row(
#     table_name='users',
#     condition='name = "John Doe"'
# )

# Fetch all rows from the users table
# rows = manager.fetch_all('SELECT * FROM users')
# print(rows)

# row = manager.select_one(
#     table_name='users',
#     condition='email = "john.new@example.com"'
# )
# print(row)

# Add a column to the users table
# manager.add_column(
#     table_name='users',
#     column_name='age',
#     data_type='INT',
#     constraints='NULL'
# )

# Delete a column from the users table
# manager.delete_column(
#     table_name='users',
#     column_name='age'
# )

# Select all data from users table
# data = manager.select('users')
# print(data)

# Drop the users table
# manager.drop_table('users')

# Close to the MySQL database
# manager.close()