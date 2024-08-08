class LiveManagerException(Exception):
    """Base exception class for LiveManager."""
    pass

class EventHandlingException(LiveManagerException):
    """Exception raised for errors in event handling."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class DatabaseAccessException(LiveManagerException):
    """Exception raised for errors accessing the database."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class SchemaChangeException(LiveManagerException):
    """Exception raised for errors detecting schema changes."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

class LogWriteException(LiveManagerException):
    """Exception raised for errors writing to the log file."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message
