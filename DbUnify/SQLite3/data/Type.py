class DataType:
    INTEGER = 'INTEGER'
    TEXT = 'TEXT'
    BLOB = 'BLOB'
    REAL = 'REAL'
    NUMERIC = 'NUMERIC'

    @staticmethod
    def CHARACTER(length: int) -> str:
        """
        Return CHARACTER type with specified length.
        """
        return f'CHAR({length})'

    @staticmethod
    def VARCHAR(length: int) -> str:
        """
        Return VARCHAR type with specified length.
        """
        return f'VARCHAR({length})'

    @staticmethod
    def NCHAR(length: int) -> str:
        """
        Return NCHAR type with specified length.
        """
        return f'NCHAR({length})'

    @staticmethod
    def NVARCHAR(length: int) -> str:
        """
        Return NVARCHAR type with specified length.
        """
        return f'NVARCHAR({length})'

    @staticmethod
    def DECIMAL(precision: int, scale: int) -> str:
        """
        Return DECIMAL type with specified precision and scale.
        """
        return f'DECIMAL({precision},{scale})'
