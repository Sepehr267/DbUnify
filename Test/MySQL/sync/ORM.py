from DbUnify.MySQL.sync import *

orm_manager = ORMManager(
    host='localhost',
    user='root',
    password='',
    database='example_db',
    port=3306,
    sql_injection_detection=False
)

class User(Model):
    id = Field(DataType.INTEGER, constraints=[Rules.PRIMARY_KEY, Rules.AUTO_INCREMENT])
    name = Field(DataType.TEXT, constraints=[Rules.NOT_NULL])
    email = Field(DataType.TEXT, constraints=[Rules.UNIQUE])
User.set_manager(orm_manager)

# Create a table using the ORM functionalities.
# User.create_table()

# Insert a row into a table.
# User.insert_row(values={'name': 'Pavel', 'email': 'Pavel@example.com'})

# Select Row
# data = User.select()
# print(data)

# Update Row
# User.update_row(
#     condition='name = John Doe',
#     values={
#         'email' : 'john@newdomain.com'
#     }
# )

# Add Column
# User.add_column(
#     'Age',
#     DataType.INTEGER,
#     [Rules.NOT_NULL]
# )

# Delete Column
# User.delete_column('Age')

# Select One Row
# data = User.select_one(
#     name='John Doe'
# )
# print(data)

# Delete Row
# User.delete_row(name='Pavel')

# Drop Table
# User.drop_table()