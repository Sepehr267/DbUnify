from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
from DbUnify.SQLite3.data import Rules, DataType

# Define a model
class User(Model):
    name = Field(data_type=DataType.TEXT)
    email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

# Create an ORMManager instance and set it for the model
orm_manager = ORMManager(db_name='example.db', sql_injection_detection=False)
User.set_manager(orm_manager)

# User.create_table()

# # Add a new column to the model's table
# User.add_column(column_name='age', data_type=DataType.INTEGER, constraints=[Rules.NOT_NULL])

# Apply schema changes
# User.alter_table_schema()

# Apply migrations
# User.apply_migrations()

# Generate table schema
# schema = User.create_table_schema()
# print(schema)

# Delete a column from the table
# User.delete_column(column_name='age')

# Drop Table
# orm_manager.drop_table('user_backup')

# Insert a row into the table
# User.insert_row({
#     'name': 'Sepehr',
#     'email': 'Sepehr@example.com'
# })

# Delete a row with a specific condition
# User.delete_row('email = ?', 'Sepehr@yahoo.com')

# Fetch all results for a query
# results = User.fetch_all('SELECT * FROM user')
# print(results)

# Get the model fields
# fields = User.get_fields()
# print(fields)

# Get ORM Manager instracne
# orm_manager_instance = User.get_orm_manager()
# print(orm_manager_instance)

# Get columns for the table
# columns = User.get_table_columns()
# print(columns)

# Get the table name
# table_name = User.get_table_name()
# print(table_name)

# Map the model to the database
# User.map_model()

# Fetch all rows from the table
# rows = User.select()
# print(rows)

# Fetch a single row based on a condition
# row = User.select_one('email = ?', 'Sepehr@example.com')
# print(row)

# Update a row in the table
# User.update_row(
#     condition= 'name = Sepehr',
#     values={'email': 'Sepehr@yahoo.com'},
# )

