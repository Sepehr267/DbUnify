from enum import Enum

class Rules(Enum):
    PRIMARY_KEY = 'PRIMARY KEY'
    AUTO_INCREMENT = 'AUTO_INCREMENT'
    NOT_NULL = 'NOT NULL'
    UNIQUE = 'UNIQUE'
    DEFAULT = lambda value: f'DEFAULT {value}'
    
    def __str__(self):
        return self.value