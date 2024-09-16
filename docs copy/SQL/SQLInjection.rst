SQL Injection
====================

This document provides examples demonstrating the use of the `SQLInjection` class to detect potential SQL injection attempts.

1. **Initialize the SQLInjection Class**

   Create an instance of the `SQLInjection` class.

   .. code-block:: python

      from DbUnify.SQL import SQLInjection

      sql_injection_detector = SQLInjection()

2. **Detect SQL Injection in a Query**

   Check if a SQL query contains any suspicious patterns that might indicate a SQL injection attempt.

   **Example 1: Suspicious Pattern Detected**

   .. code-block:: python

      query = "SELECT * FROM users WHERE username = 'admin' OR 1=1 --'"
      parameters = ()
      detected = sql_injection_detector.detect(query, *parameters)
      print(detected)

   Output:

   .. code-block::

      [SQLINJ] Potential SQL injection detected. SQL Command: SELECT * FROM users WHERE username = 'admin' OR 1=1 --', Parameters: ()

   **Example 2: No Suspicious Pattern**

   .. code-block:: python

      query = "SELECT * FROM users WHERE username = 'admin'"
      parameters = ()
      detected = sql_injection_detector.detect(query, *parameters)
      print(detected)

   Output:

   .. code-block::

      False

3. **Detect SQL Injection with Parameters**

   The `detect` method can also handle SQL queries with parameters.

   **Example 1: Suspicious Pattern with Parameters**

   .. code-block:: python

      query = "SELECT * FROM users WHERE id = ? AND name = ?"
      parameters = (1, "admin' OR 1=1 --")
      detected = sql_injection_detector.detect(query, *parameters)
      print(detected)

   Output:

   .. code-block::

      [SQLINJ] Potential SQL injection detected. SQL Command: SELECT * FROM users WHERE id = ? AND name = ?, Parameters: (1, "admin' OR 1=1 --")

   **Example 2: Safe Parameters**

   .. code-block:: python

      query = "SELECT * FROM users WHERE id = ? AND name = ?"
      parameters = (1, "admin")
      detected = sql_injection_detector.detect(query, *parameters)
      print(detected)

   Output:

   .. code-block::

      False

4. **Understand Suspicious Patterns**

   The `SQLInjection` class uses a set of patterns to detect potential SQL injection attempts. Here are some examples:

   - **Union-based Injection**

     - Pattern: `(?i)\bUNION\b\s+\bSELECT\b`

   - **Boolean-based Injection**

     - Pattern: `(?i)\bOR\b\s+1\s*=\s*1\b`

   - **Comment-based Injection**

     - Pattern: `(?i)\b--\b`

   - **SQL Server Specific Patterns**

     - Pattern: `(?i)\bEXEC\b\s+\bXP_`

   - **MySQL Specific Patterns**

     - Pattern: `(?i)\bBENCHMARK\b\s*\(\d+,.+\)`

   Each pattern represents a common SQL injection technique and helps in identifying potentially malicious queries.
