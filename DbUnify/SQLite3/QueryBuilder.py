from typing import List, Dict, Union, Optional

class QueryBuilder:
    def __init__(self):
        """
        Initializes the QueryBuilder instance.
        """
        pass
    
    def select(self, *columns: str) -> str:
        """
        Constructs a SQL SELECT clause.
        
        :param columns: Column names to be selected. If empty, '*' is used to select all columns.
        :return: SQL SELECT clause as a string.
        
        """
        columns_str = ', '.join(columns) if columns else '*'
        return f"SELECT {columns_str}"
    
    def from_table(self, table: str) -> str:
        """
        Constructs a SQL FROM clause.
        
        :param table: Name of the table to select from.
        :return: SQL FROM clause as a string.
        
        """
        return f"FROM {table}"
    
    def join(self, table: str, on_condition: str, join_type: str = 'INNER') -> str:
        """
        Constructs a SQL JOIN clause.
        
        :param table: Name of the table to join.
        :param on_condition: ON condition for the join.
        :param join_type: Type of join (e.g., 'INNER', 'LEFT', 'RIGHT'). Defaults to 'INNER'.
        :return: SQL JOIN clause as a string.
        
        """
        return f"{join_type} JOIN {table} ON {on_condition}"
    
    def where(self, *conditions: str) -> str:
        """
        Constructs a SQL WHERE clause.
        
        :param conditions: Conditions to be used in the WHERE clause.
        :return: SQL WHERE clause as a string.
        
        """
        return f"WHERE {' AND '.join(conditions)}" if conditions else ''
    
    def group_by(self, *columns: str) -> str:
        """
        Constructs a SQL GROUP BY clause.
        
        :param columns: Columns to group by.
        :return: SQL GROUP BY clause as a string.
        
        """
        return f"GROUP BY {', '.join(columns)}" if columns else ''
    
    def having(self, *conditions: str) -> str:
        """
        Constructs a SQL HAVING clause.
        
        :param conditions: Conditions to be used in the HAVING clause.
        :return: SQL HAVING clause as a string.
        
        """
        return f"HAVING {' AND '.join(conditions)}" if conditions else ''
    
    def order_by(self, *columns: str) -> str:
        """
        Constructs a SQL ORDER BY clause.
        
        :param columns: Columns to order by, with optional sorting direction (e.g., 'ASC', 'DESC').
        :return: SQL ORDER BY clause as a string.
        
        """
        return f"ORDER BY {', '.join(columns)}" if columns else ''
    
    def limit(self, limit: Optional[int] = None) -> str:
        """
        Constructs a SQL LIMIT clause.
        
        :param limit: Maximum number of rows to return.
        :return: SQL LIMIT clause as a string.
        
        """
        return f"LIMIT {limit}" if limit is not None else ''
    
    def offset(self, offset: Optional[int] = None) -> str:
        """
        Constructs a SQL OFFSET clause.
        
        :param offset: Number of rows to skip before starting to return rows.
        :return: SQL OFFSET clause as a string.
        
        """
        return f"OFFSET {offset}" if offset is not None else ''
    
    def insert_into(self, table: str) -> str:
        """
        Constructs a SQL INSERT INTO clause.
        
        :param table: Name of the table to insert into.
        :return: SQL INSERT INTO clause as a string.
        
        """
        return f"INSERT INTO {table}"
    
    def values(self, **values: Union[str, int, float, bool]) -> str:
        """
        Constructs a SQL VALUES clause.
        
        :param values: Column-value pairs to be inserted.
        :return: SQL VALUES clause as a string.
        
        """
        columns = ', '.join(values.keys())
        values_str = ', '.join(repr(v) for v in values.values())
        return f"({columns}) VALUES ({values_str})"
    
    def update(self, table: str) -> str:
        """
        Constructs a SQL UPDATE clause.
        
        :param table: Name of the table to update.
        :return: SQL UPDATE clause as a string.
        
        """
        return f"UPDATE {table}"
    
    def set(self, **values: Union[str, int, float, bool]) -> str:
        """
        Constructs a SQL SET clause for updating rows.
        
        :param values: Column-value pairs to be updated.
        :return: SQL SET clause as a string.
        
        """
        set_clause = ', '.join(f"{col} = {repr(val)}" for col, val in values.items())
        return f"SET {set_clause}" if values else ''
    
    def delete_from(self, table: str) -> str:
        """
        Constructs a SQL DELETE FROM clause.
        
        :param table: Name of the table to delete from.
        :return: SQL DELETE FROM clause as a string.
        
        """
        return f"DELETE FROM {table}"
    
    def delete_where(self, *conditions: str) -> str:
        """
        Constructs a SQL WHERE clause for deletion.
        
        :param conditions: Conditions to be used in the WHERE clause.
        :return: SQL WHERE clause for deletion as a string.
        
        """
        return f"WHERE {' AND '.join(conditions)}" if conditions else ''
    
    def create_table(self, table: str, **columns: str) -> str:
        """
        Constructs a SQL CREATE TABLE clause.
        
        :param table: Name of the table to be created.
        :param columns: Column definitions, where keys are column names and values are data types.
        :return: SQL CREATE TABLE clause as a string.
        
        """
        columns_str = ', '.join(f"{col} {type_}" for col, type_ in columns.items())
        return f"CREATE TABLE {table} ({columns_str})"
    
    def alter_table(self, table: str, commands: List[str]) -> str:
        """
        Constructs a SQL ALTER TABLE clause.
        
        :param table: Name of the table to be altered.
        :param commands: List of commands to modify the table structure (e.g., adding or dropping columns).
        :return: SQL ALTER TABLE clause as a string.
        
        Example:
        >>> qb = QueryBuilder()
        >>> qb.alter_table(
        ...     table='products',
        ...     commands=['ADD COLUMN description TEXT', 'DROP COLUMN stock']
        ... )
        'ALTER TABLE products ADD COLUMN description TEXT, DROP COLUMN stock'
        """
        return f"ALTER TABLE {table} {', '.join(commands)}"
    
    def drop_table(self, table: str) -> str:
        """
        Constructs a SQL DROP TABLE clause.
        
        :param table: Name of the table to be dropped.
        :return: SQL DROP TABLE clause as a string.
        
        Example:
        >>> qb = QueryBuilder()
        >>> qb.drop_table('old_users')
        'DROP TABLE old_users'
        """
        return f"DROP TABLE {table}"

    def delete_where(self, *conditions: str) -> str:
        """
        Constructs a SQL WHERE clause for deletion.
        
        :param conditions: Conditions to be used in the WHERE clause.
        :return: SQL WHERE clause for deletion as a string.
        
        Example:
        >>> qb = QueryBuilder()
        >>> qb.delete_where('age < 18')
        'WHERE age < 18'
        """
        return f"WHERE {' AND '.join(conditions)}" if conditions else ''
    
    def create_table(self, table: str, **columns: str) -> str:
        """
        Constructs a SQL CREATE TABLE clause.
        
        :param table: Name of the table to be created.
        :param columns: Column definitions, where keys are column names and values are data types.
        :return: SQL CREATE TABLE clause as a string.
        
        Example:
        >>> qb = QueryBuilder()
        >>> qb.create_table(
        ...     table='products',
        ...     id='INTEGER PRIMARY KEY',
        ...     name='TEXT NOT NULL',
        ...     price='REAL',
        ...     stock='INTEGER DEFAULT 0'
        ... )
        'CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price REAL, stock INTEGER DEFAULT 0)'
        """
        columns_str = ', '.join(f"{col} {type_}" for col, type_ in columns.items())
        return f"CREATE TABLE {table} ({columns_str})"
    
    def alter_table(self, table: str, commands: List[str]) -> str:
        """
        Constructs a SQL ALTER TABLE clause.
        
        :param table: Name of the table to be altered.
        :param commands: List of commands to modify the table structure (e.g., adding or dropping columns).
        :return: SQL ALTER TABLE clause as a string.
        
        """
        return f"ALTER TABLE {table} {', '.join(commands)}"
    
    def drop_table(self, table: str) -> str:
        """
        Constructs a SQL DROP TABLE clause.
        
        :param table: Name of the table to be dropped.
        :return: SQL DROP TABLE clause as a string.
        
        """
        return f"DROP TABLE {table}"
    
    def truncate_table(self, table: str) -> str:
        """
        Constructs a SQL TRUNCATE TABLE clause.
        
        :param table: Name of the table to be truncated.
        :return: SQL TRUNCATE TABLE clause as a string.
        
        """
        return f"TRUNCATE TABLE {table}"
    
    def union(self, *queries: str) -> str:
        """
        Constructs a SQL UNION clause to combine the results of multiple SELECT queries.
        
        :param queries: SQL SELECT queries to be combined with UNION.
        :return: SQL UNION clause as a string.
        
        """
        return f"({') UNION ('.join(queries)})"
    
    def exists(self, subquery: str) -> str:
        """
        Constructs a SQL EXISTS clause to check for the existence of rows returned by a subquery.
        
        :param subquery: SQL query to be checked for existence.
        :return: SQL EXISTS clause as a string.
        
        """
        return f"EXISTS ({subquery})"
    
    def subquery(self, query: str) -> str:
        """
        Wraps a query in parentheses to be used as a subquery.
        
        :param query: SQL query to be wrapped as a subquery.
        :return: SQL subquery as a string.
        
        """
        return f"({query})"
    
    def get_select_query(self, table: str, columns: Optional[List[str]] = None, 
                         joins: Optional[List[str]] = None,
                         conditions: Optional[List[str]] = None, 
                         group_by: Optional[List[str]] = None,
                         having: Optional[List[str]] = None, 
                         order_by: Optional[List[str]] = None,
                         limit: Optional[int] = None, 
                         offset: Optional[int] = None) -> str:
        """
        Constructs a complete SQL SELECT query.
        
        :param table: Name of the table to select from.
        :param columns: List of columns to select. If None, all columns are selected.
        :param joins: List of JOIN clauses to be added to the query.
        :param conditions: List of WHERE conditions to be applied.
        :param group_by: List of columns to group by.
        :param having: List of HAVING conditions.
        :param order_by: List of columns to order by, with optional sorting direction.
        :param limit: Number of rows to return.
        :param offset: Number of rows to skip before starting to return rows.
        :return: Complete SQL SELECT query as a string.
        
        """
        columns = columns or []
        joins = joins or []
        conditions = conditions or []
        group_by = group_by or []
        having = having or []
        order_by = order_by or []
        
        query = f"{self.select(*columns)} {self.from_table(table)}"
        if joins:
            query += ' ' + ' '.join(joins)
        if conditions:
            query += ' ' + self.where(*conditions)
        if group_by:
            query += ' ' + self.group_by(*group_by)
        if having:
            query += ' ' + self.having(*having)
        if order_by:
            query += ' ' + self.order_by(*order_by)
        if limit is not None:
            query += ' ' + self.limit(limit)
        if offset is not None:
            query += ' ' + self.offset(offset)
        return query
    
    def get_insert_query(self, table: str, **values: Union[str, int, float, bool]) -> str:
        """
        Constructs a complete SQL INSERT query.
        
        :param table: Name of the table to insert into.
        :param values: Column-value pairs to be inserted.
        :return: Complete SQL INSERT query as a string.
        
        """
        return f"{self.insert_into(table)} {self.values(**values)}"
    
    def get_update_query(self, table: str, values: Dict[str, Union[str, int, float, bool]],
                         conditions: Optional[List[str]] = None) -> str:
        """
        Constructs a complete SQL UPDATE query.
        
        :param table: Name of the table to update.
        :param values: Column-value pairs to be updated.
        :param conditions: List of WHERE conditions to be applied.
        :return: Complete SQL UPDATE query as a string.
        
        """
        conditions = conditions or []
        query = f"{self.update(table)} {self.set(**values)}"
        if conditions:
            query += ' ' + self.where(*conditions)
        return query
    
    def get_delete_query(self, table: str, conditions: Optional[List[str]] = None) -> str:
        """
        Constructs a complete SQL DELETE query.
        
        :param table: Name of the table to delete from.
        :param conditions: List of WHERE conditions to be applied.
        :return: Complete SQL DELETE query as a string.
        
        """
        conditions = conditions or []
        query = f"{self.delete_from(table)}"
        if conditions:
            query += ' ' + self.delete_where(*conditions)
        return query
