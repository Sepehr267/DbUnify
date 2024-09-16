from ...data.Rules import Rules
from typing import List, Optional, Union

class Field:
    """
    Base class for all model fields.
    """
    def __init__(self, data_type: str, constraints: Optional[List[Union[str, Rules]]] = None):
        self.data_type = data_type
        self.constraints = constraints or []
