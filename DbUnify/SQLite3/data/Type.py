
class DataType:
    INT = 'INT'
    INTEGER = 'INTEGER'
    TINYINT = 'TINYINT'
    SMALLINT = 'SMALLINT'
    MEDIUMINT = 'MEDIUMINT'
    BIGINT = 'BIGINT'
    UNSIGNED_BIG_INT = 'UNSIGNED BIG INT'
    INT2 = 'INT2'
    INT8 = 'INT8'
    TEXT = 'TEXT'
    CLOB = 'CLOB'
    BLOB = 'BLOB'
    REAL = 'REAL'
    DOUBLE = 'DOUBLE'
    DOUBLE_PRECISION = 'DOUBLE PRECISION'
    FLOAT = 'FLOAT'
    NUMERIC = 'NUMERIC'
    BOOLEAN = 'BOOLEAN'
    DATE = 'DATE'
    DATETIME = 'DATETIME'
    NONE = ''
    
    @staticmethod
    def CHARACTER(length: int) -> str:
        return f'CHARACTER({length})'

    @staticmethod
    def VARCHAR(length: int) -> str:
        return f'VARCHAR({length})'

    @staticmethod
    def VARYING_CHARACTER(length: int) -> str:
        return f'VARYING CHARACTER({length})'

    @staticmethod
    def NCHAR(length: int) -> str:
        return f'NCHAR({length})'

    @staticmethod
    def NATIVE_CHARACTER(length: int) -> str:
        return f'NATIVE CHARACTER({length})'

    @staticmethod
    def NVARCHAR(length: int) -> str:
        return f'NVARCHAR({length})'

    @staticmethod
    def DECIMAL(precision: int, scale: int) -> str:
        return f'DECIMAL({precision},{scale})'
