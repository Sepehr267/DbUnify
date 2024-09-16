QueryBuilder Example
====================

This document provides examples demonstrating the use of each method in the `QueryBuilder` class to construct SQL queries.

1. **SELECT Clause**

   Constructs a SQL `SELECT` clause.

   .. code-block:: python

      from DbUnify.MySQL import QueryBuilder
      qb = QueryBuilder()
      query = qb.select("id", "name", "salary")
      print(query)

   Output:

   .. code-block::

      SELECT id, name, salary

2. **FROM Clause**

   Constructs a SQL `FROM` clause.

   .. code-block:: python

      qb = QueryBuilder()
      query = qb.from_table("employees")
      print(query)

   Output:

   .. code-block::

      FROM employees

3. **JOIN Clause**

   Constructs a SQL `JOIN` clause.

   .. code-block:: python

      qb = QueryBuilder()
      query = qb.join("departments", "employees.department_id = departments.id", "LEFT")
      print(query)

   Output:

   .. code-block::

      LEFT JOIN departments ON employees.department_id = departments.id

4. **WHERE Clause**

   Constructs a SQL `WHERE` clause.

   .. code-block:: python

      qb = QueryBuilder()
      query = qb.where("salary > 50000", "department_id = 3")
      print(query)

   Output:

   .. code-block::

      WHERE salary > 50000 AND department_id = 3

5. **GROUP BY Clause**

   Constructs a SQL `GROUP BY` clause.

   .. code-block:: python

      qb = QueryBuilder()
      query = qb.group_by("department_id")
      print(query)

   Output:

   .. code-block::

      GROUP BY department_id

6. **HAVING Clause**

   Constructs a SQL `HAVING` clause.

   .. code-block:: python

      qb = QueryBuilder()
      query = qb.having("COUNT(id) > 5")
      print(query)

   Output:

   .. code-block::

      HAVING COUNT(id) > 5

7. **ORDER BY Clause**

   Constructs a SQL `ORDER BY` clause.

   .. code-block:: python

      qb = QueryBuilder()
      query = qb.order_by("salary DESC", "name ASC")
      print(query)

   Output:

   .. code-block::

      ORDER BY salary DESC, name ASC

8. **LIMIT Clause**

   Constructs a SQL `LIMIT` clause.

   .. code-block:: python

      qb = QueryBuilder()
      query = qb.limit(10)
      print(query)

   Output:

   .. code-block::

      LIMIT 10

9. **OFFSET Clause**

   Constructs a SQL `OFFSET` clause.

   .. code-block:: python

      qb = QueryBuilder()
      query = qb.offset(20)
      print(query)

   Output:

   .. code-block::

      OFFSET 20

10. **INSERT INTO Clause**

    Constructs a SQL `INSERT INTO` clause.

    .. code-block:: python

       qb = QueryBuilder()
       query = qb.insert_into("employees")
       print(query)

    Output:

    .. code-block::

       INSERT INTO employees

11. **VALUES Clause**

    Constructs a SQL `VALUES` clause.

    .. code-block:: python

       qb = QueryBuilder()
       query = qb.values(id=1, name="John Doe", salary=60000, department_id=3)
       print(query)

    Output:

    .. code-block::

       (id, name, salary, department_id) VALUES (1, 'John Doe', 60000, 3)

12. **UPDATE Clause**

    Constructs a SQL `UPDATE` clause.

    .. code-block:: python

       qb = QueryBuilder()
       query = qb.update("employees")
       print(query)

    Output:

    .. code-block::

       UPDATE employees

13. **SET Clause**

    Constructs a SQL `SET` clause.

    .. code-block:: python

       qb = QueryBuilder()
       query = qb.set(name="Jane Doe", salary=65000)
       print(query)

    Output:

    .. code-block::

       SET name = 'Jane Doe', salary = 65000

14. **DELETE FROM Clause**

    Constructs a SQL `DELETE FROM` clause.

    .. code-block:: python

       qb = QueryBuilder()
       query = qb.delete_from("employees")
       print(query)

    Output:

    .. code-block::

       DELETE FROM employees

15. **TRUNCATE TABLE Clause**

    Constructs a SQL `TRUNCATE TABLE` clause.

    .. code-block:: python

       qb = QueryBuilder()
       query = qb.truncate_table("employees")
       print(query)

    Output:

    .. code-block::

       TRUNCATE TABLE employees

16. **UNION Clause**

    Constructs a SQL `UNION` clause to combine results from multiple queries.

    .. code-block:: python

       qb = QueryBuilder()
       query1 = qb.select("id", "name").from_table("employees")
       query2 = qb.select("id", "name").from_table("contractors")
       query = qb.union(query1, query2)
       print(query)

    Output:

    .. code-block::

       (SELECT id, name FROM employees) UNION (SELECT id, name FROM contractors)

17. **EXISTS Clause**

    Constructs a SQL `EXISTS` clause to check for the existence of rows.

    .. code-block:: python

       qb = QueryBuilder()
       subquery = qb.select("id").from_table("employees").where("salary > 50000")
       query = qb.exists(subquery)
       print(query)

    Output:

    .. code-block::

       EXISTS (SELECT id FROM employees WHERE salary > 50000)

18. **Subquery**

    Wraps a query in parentheses to be used as a subquery.

    .. code-block:: python

       qb = QueryBuilder()
       query = qb.subquery(qb.select("id", "name").from_table("employees"))
       print(query)

    Output:

    .. code-block::

       (SELECT id, name FROM employees)

19. **Complete SELECT Query**

    Constructs a complete SQL `SELECT` query.

    .. code-block:: python

       qb = QueryBuilder()
       query = qb.get_select_query(
           table="employees",
           columns=["id", "name", "salary"],
           joins=[
               qb.join("departments", "employees.department_id = departments.id", "LEFT")
           ],
           conditions=["salary > 50000", "departments.name = 'Engineering'"],
           group_by=["departments.name"],
           having=["COUNT(employees.id) > 5"],
           order_by=["salary DESC"],
           limit=10,
           offset=20
       )
       print(query)

    Output:

    .. code-block::

       SELECT id, name, salary FROM employees
       LEFT JOIN departments ON employees.department_id = departments.id
       WHERE salary > 50000 AND departments.name = 'Engineering'
       GROUP BY departments.name
       HAVING COUNT(employees.id) > 5
       ORDER BY salary DESC
       LIMIT 10
       OFFSET 20

20. **Complete INSERT Query**

    Constructs a complete SQL `INSERT` query.

    .. code-block:: python

       qb = QueryBuilder()
       query = qb.get_insert_query(
           table="employees",
           id=1,
           name="John Doe",
           salary=60000,
           department_id=3
       )
       print(query)

    Output:

    .. code-block::

       INSERT INTO employees (id, name, salary, department_id) VALUES (1, 'John Doe', 60000, 3)

21. **Complete UPDATE Query**

    Constructs a complete SQL `UPDATE` query.

    .. code-block:: python

       qb = QueryBuilder()
       query = qb.get_update_query(
           table="employees",
           values={"salary": 65000},
           conditions=["id = 1"]
       )
       print(query)

    Output:

    .. code-block::

       UPDATE employees SET salary = 65000 WHERE id = 1

22. **Complete DELETE Query**

    Constructs a complete SQL `DELETE` query.

    .. code-block:: python

       qb = QueryBuilder()
       query = qb.get_delete_query(
           table="employees",
           conditions=["id = 1"]
       )
       print(query)

    Output:

    .. code-block::

       DELETE FROM employees WHERE id = 1
