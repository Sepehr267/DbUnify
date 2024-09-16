from typing import Dict

class Attribute:
    def __init__(self, timestamp: str, db_name: str, table_name: str, operation: str, command: str, details: dict):
        self.timestamp = timestamp
        self.db_name = db_name
        self.table_name = table_name
        self.operation = operation
        self.command = command
        self.details = details

    def to_dict(self) -> Dict:
        """Convert the Attribute object to a dictionary."""
        return {
            'timestamp': self.timestamp,
            'db_name': self.db_name,
            'table_name': self.table_name,
            'operation': self.operation,
            'command': self.command,
            'details': self.details
        }

    def __repr__(self) -> str:
        return f"<Change(timestamp={self.timestamp}, db_name={self.db_name}, table_name={self.table_name}, operation={self.operation}, command={self.command}, details={self.details})>"
