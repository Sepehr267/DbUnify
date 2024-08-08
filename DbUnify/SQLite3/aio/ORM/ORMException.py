class ORMMException(Exception):
    """
    Base class for all exceptions related to the Manager and ORM system.
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)
