DbUnify documentation
=====================

DbUnify provides a comprehensive suite of features for working with both SQLite and MySQL databases. Below is an overview of its capabilities:

- **Support for SQLite3**: This library supports the SQLite3 database engine.
- **Support for MySQL**: The library includes support for the MySQL database engine, with all capabilities available except for live listening in both synchronous and asynchronous contexts.
- **ORM Support**: It includes support for Object-Relational Mapping (ORM) to simplify database interactions.
- **Query Builder**: A robust query builder is available for constructing SQLite and MySQL commands. Note that it does not support async operations.
- **Cache Methods**: Utilize caching methods to save and retrieve data efficiently.
- **Export Data**: Export data to Charts and CSV formats for easy data visualization and sharing.
- **Support for Async**: The library supports asynchronous operations in various contexts.
- **Async ORM Support**: Provides support for asynchronous ORM operations, enhancing performance and scalability.
- **Performance**: It is up to twice as fast as SQLAlchemy, making it a high-performance option for database interactions.
- **Database Listening**: Users can listen for real-time changes in the database. Note that this feature does not support async operations.
- **Full SQL Capability**: The library supports all SQL functionalities, ensuring comprehensive database management.
- **SQL Query Checker (SQC)**: An AI-powered feature for checking SQL queries for various issues.
- **SQL Injection Checker**: Detects potential SQL injection vulnerabilities in queries.

**Note**: All features except for database listening and live listening for MySQL are compatible with async operations.

.. toctree::
   :maxdepth: 2
   :caption: DbUnify:

   SQLite3
   MySQL
   SQL
