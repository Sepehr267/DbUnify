Query Builder
==============

This module provides functionalities for exporting data in synchronous contexts.

.. automodule:: DbUnify.SQLite3.QueryBuilder
   :members:
   :undoc-members:
   :show-inheritance:

The `QueryBuilder` class provides functionalities to construct SQL queries. Below are examples of how to use each method in the `QueryBuilder` class.

**Class Initialization**

First, import the necessary module and initialize the `QueryBuilder` class.

.. code-block:: python

    from DbUnify.SQLite3.QueryBuilder import QueryBuilder

    qb = QueryBuilder()

**Method Examples**

**1. `alter_table`**

Constructs a SQL `ALTER TABLE` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.alter_table(
        table='employees',
        commands=[
            'ADD COLUMN salary REAL',
            'DROP COLUMN old_position'
        ]
    )
    print(sql)

.. code-block::

    ALTER TABLE employees ADD COLUMN salary REAL, DROP COLUMN old_position

**2. `create_table`**

Constructs a SQL `CREATE TABLE` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.create_table(
        table='products',
        id='INTEGER PRIMARY KEY',
        name='TEXT NOT NULL',
        price='REAL',
        stock='INTEGER DEFAULT 0'
    )
    print(sql)

.. code-block::

    CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL, stock INTEGER DEFAULT 0)

**3. `delete_from`**

Constructs a SQL `DELETE FROM` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.delete_from(table='employees')
    print(sql)

.. code-block::

    DELETE FROM employees

**4. `delete_where`**

Constructs a SQL `WHERE` clause for deletion.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.delete_where('age < 18')
    print(sql)

.. code-block::

    WHERE age < 18

**5. `drop_table`**

Constructs a SQL `DROP TABLE` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.drop_table(table='old_data')
    print(sql)

.. code-block::

    DROP TABLE old_data

**6. `exists`**

Constructs a SQL `EXISTS` clause to check for the existence of rows returned by a subquery.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.exists(subquery='SELECT 1 FROM employees WHERE id = 1')
    print(sql)

.. code-block::

    EXISTS (SELECT 1 FROM employees WHERE id = 1)

**7. `from_table`**

Constructs a SQL `FROM` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.from_table(table='employees')
    print(sql)

.. code-block::

    FROM employees

**8. `get_delete_query`**

Constructs a complete SQL `DELETE` query.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.get_delete_query(
        table='employees',
        conditions=['age < 18']
    )
    print(sql)

.. code-block::

    DELETE FROM employees WHERE age < 18

**9. `get_insert_query`**

Constructs a complete SQL `INSERT` query.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.get_insert_query(
        table='employees',
        name='John Doe',
        age=30,
        department='HR'
    )
    print(sql)

.. code-block::

    INSERT INTO employees (name, age, department) VALUES ('John Doe', 30, 'HR')

**10. `get_select_query`**

Constructs a complete SQL `SELECT` query.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.get_select_query(
        table='employees',
        columns=['name', 'age'],
        conditions=['age > 30'],
        order_by=['name DESC'],
        limit=10
    )
    print(sql)

.. code-block::

    SELECT name, age FROM employees WHERE age > 30 ORDER BY name DESC LIMIT 10

**11. `get_update_query`**

Constructs a complete SQL `UPDATE` query.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.get_update_query(
        table='employees',
        values={'department': 'Sales'},
        conditions=['id = 1']
    )
    print(sql)

.. code-block::

    UPDATE employees SET department = 'Sales' WHERE id = 1

**12. `group_by`**

Constructs a SQL `GROUP BY` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.group_by('department')
    print(sql)

.. code-block::

    GROUP BY department

**13. `having`**

Constructs a SQL `HAVING` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.having('COUNT(*) > 5')
    print(sql)

.. code-block::

    HAVING COUNT(*) > 5

**14. `insert_into`**

Constructs a SQL `INSERT INTO` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.insert_into(table='employees')
    print(sql)

.. code-block::

    INSERT INTO employees

**15. `join`**

Constructs a SQL `JOIN` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.join(table='departments', on_condition='employees.department_id = departments.id', join_type='LEFT')
    print(sql)

.. code-block::

    LEFT JOIN departments ON employees.department_id = departments.id

**16. `limit`**

Constructs a SQL `LIMIT` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.limit(limit=5)
    print(sql)

.. code-block::

    LIMIT 5

**17. `offset`**

Constructs a SQL `OFFSET` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.offset(offset=10)
    print(sql)

.. code-block::

    OFFSET 10

**18. `order_by`**

Constructs a SQL `ORDER BY` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.order_by('age DESC', 'name ASC')
    print(sql)

.. code-block::

    ORDER BY age DESC, name ASC

**19. `select`**

Constructs a SQL `SELECT` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.select('name', 'age')
    print(sql)

.. code-block::

    SELECT name, age

**20. `set`**

Constructs a SQL `SET` clause for updating rows.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.set(name='Jane Doe', age=32)
    print(sql)

.. code-block::

    SET name = 'Jane Doe', age = 32

**21. `subquery`**

Wraps a query in parentheses to be used as a subquery.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.subquery('SELECT * FROM employees WHERE age > 30')
    print(sql)

.. code-block::

    (SELECT * FROM employees WHERE age > 30)

**22. `truncate_table`**

Constructs a SQL `TRUNCATE TABLE` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.truncate_table(table='old_records')
    print(sql)

.. code-block::

    TRUNCATE TABLE old_records

**23. `union`**

Constructs a SQL `UNION` clause to combine the results of multiple SELECT queries.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.union(
        'SELECT name FROM employees WHERE department = "HR"',
        'SELECT name FROM contractors WHERE department = "HR"'
    )
    print(sql)

.. code-block::

    SELECT name FROM employees WHERE department = 'HR' UNION SELECT name FROM contractors WHERE department = 'HR'

**24. `update`**

Constructs a SQL `UPDATE` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.update(table='employees')
    print(sql)

.. code-block::

    UPDATE employees

**25. `values`**

Constructs a SQL `VALUES` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.values(name='Alice', age=29)
    print(sql)

.. code-block::

    VALUES (name = 'Alice', age = 29)

**26. `where`**

Constructs a SQL `WHERE` clause.

.. code-block:: python

    qb = QueryBuilder()
    sql = qb.where('age > 30', 'department = "Sales"')
    print(sql)

.. code-block::

    WHERE age > 30 AND department = 'Sales'
