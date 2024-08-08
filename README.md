# DbUnify | Database Management

**DbUnify** (Database Management) is a versatile Python library that simplifies database connectivity and management using SQLite.

## Installation
   Install the DbUnify library from PyPI or GitHub.
   
   ```bash
   pip install DbUnify
   ```
## Create a Database
```python
from DbUnify.SQLite3.sync.ORM import Model, ORMManager, Field
from DbUnify.SQLite3.data import Rules, DataType

# Define a model
class User(Model):
    name = Field(data_type=DataType.TEXT)
    email = Field(data_type=DataType.TEXT, constraints=[Rules.UNIQUE])

# Create an ORMManager instance and set it for the model
orm_manager = ORMManager(db_name='example.db')
User.set_manager(orm_manager)

# Create the table
User.create_table()
   ```


## Documentation DbUnify:

   For more information and advanced usage, refer to the [DbUnify documentation](https://DbUnify.readthedocs.io).

  
## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Sepehr0267/DbUnify/blob/main/LICENSE) file for details.

<a href="https://pypi.org/project/DbUnify/"><img src="https://img.shields.io/badge/DbUnify-2.1.2-blue"></a> 

## Developer
- **Telegram**: [t.me/Sepehr0Day](https://t.me/Sepehr0Day)

---

*Your Database Management DbUnify, made easy with DbUnify.*
