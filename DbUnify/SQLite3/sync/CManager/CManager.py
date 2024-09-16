from ctypes import c_char_p, c_int, c_void_p, CFUNCTYPE, POINTER
from typing import Optional, Callable, List, Tuple, Dict
from .CMCache import CMCache
import ctypes

CallbackType = CFUNCTYPE(c_int, c_void_p, c_int, POINTER(c_char_p), POINTER(c_char_p))

class CManager:
    def __init__(self, dll_path: str, cache_ttl: int = 60, cache_size: int = 1000) -> None:
        """
        Initialize the CManager with a DLL path and optional cache settings.

        :param dll_path: Path to the shared library (DLL).
        :param cache_ttl: Time-to-live for cache entries in seconds.
        :param cache_size: Maximum number of items to store in cache.
        """
        print("\033[93mNote: CManager does not support DataType and Rules classes\n\033[0m")
        self.dll = ctypes.CDLL(dll_path)
        self.db: Optional[c_void_p] = None
        self.cache = CMCache(ttl=cache_ttl, max_size=cache_size)
        self._setup_dll()

    def _setup_dll(self) -> None:
        """
        Set up the DLL function prototypes.
        """
        func_names = [
            'connect_db', 'close_db', 'execute_query', 'create_table',
            'drop_table', 'add_column', 'insert_row', 'delete_row',
            'update_row', 'get_table_columns'
        ]
        self.dll_functions: Dict[str, ctypes.CFUNCTYPE] = {}
        for func_name in func_names:
            func = getattr(self.dll, func_name)
            func.argtypes = self._get_argtypes(func_name)
            func.restype = c_int
            self.dll_functions[func_name] = func

    def _get_argtypes(self, func_name: str) -> List[type]:
        """
        Get the argument types for a given function name.

        :param func_name: The name of the function.
        :return: List of argument types.
        """
        argtypes = {
            'connect_db': [POINTER(c_void_p), c_char_p],
            'close_db': [c_void_p],
            'execute_query': [c_void_p, c_char_p, CallbackType, c_void_p],
            'create_table': [c_void_p, c_char_p, c_char_p],
            'drop_table': [c_void_p, c_char_p],
            'add_column': [c_void_p, c_char_p, c_char_p, c_char_p, c_char_p],
            'insert_row': [c_void_p, c_char_p, c_char_p],
            'delete_row': [c_void_p, c_char_p, c_char_p],
            'update_row': [c_void_p, c_char_p, c_char_p, c_char_p],
            'get_table_columns': [c_void_p, c_char_p]
        }
        return argtypes.get(func_name, [])

    def simple_callback(self, data: c_void_p, argc: c_int, argv: POINTER(c_char_p), azColName: POINTER(c_char_p)) -> c_int:
        """
        A simple callback function for use with ctypes.

        :param data: User-defined data passed to the callback.
        :param argc: Number of columns.
        :param argv: Array of column values.
        :param azColName: Array of column names.
        :return: Status code (0 for success).
        """
        return 0

    def connect_db(self, db_name: str) -> bool:
        """
        Connect to the database.

        :param db_name: The name of the database file.
        :return: True if connection was successful, False otherwise.
        """
        if self.db is not None:
            raise RuntimeError("Already connected to a database.")
        db_name_bytes = db_name.encode('utf-8')
        self.db = c_void_p()
        result = self.dll.connect_db(ctypes.byref(self.db), db_name_bytes)
        return result == 0

    def close_db(self) -> None:
        """
        Close the database connection.
        """
        if self.db is None:
            raise RuntimeError("No database connection to close.")
        self.dll.close_db(self.db)
        self.db = None

    def execute_query(self, query: str, callback: Optional[Callable[[c_void_p, int, Optional[List[str]], Optional[List[str]]], int]] = None, data: Optional[c_void_p] = None) -> int:
        """
        Execute a query against the database.

        :param query: SQL query to execute.
        :param callback: Optional callback function to handle query results.
        :param data: Optional user-defined data to pass to the callback.
        :return: Status code from the DLL function.
        """
        query_bytes = query.encode('utf-8')
        c_callback = CallbackType(callback) if callback else CallbackType(self.simple_callback)
        return self.dll.execute_query(self.db, query_bytes, c_callback, data)

    def create_table(self, table_name: str, columns: List[Tuple[str, str, List[str]]]) -> bool:
        """
        Create a new table in the database.

        :param table_name: The name of the table.
        :param columns: List of column definitions.
        :return: True if the table was created successfully, False otherwise.
        """
        columns_def = ', '.join(
            f"{name} {dtype} {' '.join(constraints)}" for name, dtype, constraints in columns
        )
        result = self.dll.create_table(self.db, table_name.encode('utf-8'), columns_def.encode('utf-8'))
        return result == 0

    def drop_table(self, table_name: str) -> bool:
        """
        Drop an existing table from the database.

        :param table_name: The name of the table to drop.
        :return: True if the table was dropped successfully, False otherwise.
        """
        result = self.dll.drop_table(self.db, table_name.encode('utf-8'))
        return result == 0

    def add_column(self, table_name: str, column_name: str, data_type: str, constraints: List[str]) -> bool:
        """
        Add a new column to an existing table.

        :param table_name: The name of the table.
        :param column_name: The name of the new column.
        :param data_type: Data type of the new column.
        :param constraints: List of constraints for the new column.
        :return: True if the column was added successfully, False otherwise.
        """
        result = self.dll.add_column(
            self.db,
            table_name.encode('utf-8'),
            column_name.encode('utf-8'),
            data_type.encode('utf-8'),
            ' '.join(constraints).encode('utf-8')
        )
        return result == 0

    def insert_row(self, table_name: str, values: Dict[str, str]) -> bool:
        """
        Insert a new row into a table.

        :param table_name: The name of the table.
        :param values: Dictionary of column names and values to insert.
        :return: True if the row was inserted successfully, False otherwise.
        """
        columns = ', '.join(values.keys())
        values_str = ', '.join(f"'{v}'" for v in values.values())
        sql_statement = f"INSERT INTO {table_name} ({columns}) VALUES ({values_str})"
        print(f"SQL Statement for insert_row: {sql_statement}")

        result = self.dll.execute_query(self.db, sql_statement.encode('utf-8'), CallbackType(self.simple_callback), None)
        return result == 0

    def delete_row(self, table_name: str, condition: str) -> bool:
        """
        Delete rows from a table based on a condition.

        :param table_name: The name of the table.
        :param condition: SQL condition to specify which rows to delete.
        :return: True if the rows were deleted successfully, False otherwise.
        """
        result = self.dll.delete_row(self.db, table_name.encode('utf-8'), condition.encode('utf-8'))
        return result == 0

    def update_row(self, table_name: str, values: Dict[str, str], condition: str) -> bool:
        """
        Update rows in a table based on a condition.

        :param table_name: The name of the table.
        :param values: Dictionary of column names and new values.
        :param condition: SQL condition to specify which rows to update.
        :return: True if the rows were updated successfully, False otherwise.
        """
        set_clause = ', '.join(f"{col} = '{val}'" for col, val in values.items())
        result = self.dll.update_row(
            self.db,
            table_name.encode('utf-8'),
            set_clause.encode('utf-8'),
            condition.encode('utf-8')
        )
        return result == 0

    def get_table_columns(self, table_name: str) -> Optional[List[str]]:
        """
        Retrieve the column names of a table.

        :param table_name: The name of the table.
        :return: List of column names if successful, None otherwise.
        """
        result = self.dll.get_table_columns(self.db, table_name.encode('utf-8'))
        return result

    def fetch_all(self, query: str) -> Optional[List[Dict[str, str]]]:
        """
        Execute a query and fetch all results.

        :param query: SQL query to execute.
        :return: List of dictionaries with column names as keys and column values as values, or None if an error occurs.
        """
        results = []

        def fetch_callback(data: c_void_p, argc: c_int, argv: POINTER(c_char_p), azColName: POINTER(c_char_p)) -> c_int:
            nonlocal results
            row = {}
            for i in range(argc):
                col_name = azColName[i].decode('utf-8') if azColName[i] else ''
                col_value = argv[i].decode('utf-8') if argv[i] else ''
                row[col_name] = col_value
            results.append(row)
            return 0

        result_code = self.execute_query(query, callback=fetch_callback)
        if result_code != 0:
            print(f"\033[91mError executing query. Status code: {result_code}\033[0m")
            return None

        return results
