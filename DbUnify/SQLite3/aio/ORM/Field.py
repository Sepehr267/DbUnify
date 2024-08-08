from typing import List, Optional, Union
from ...data.Rules import Rules

class Field:
    """
    Base class for all model fields.
    """
    def __init__(self, data_type: str, constraints: Optional[List[Union[str, Rules]]] = None):
        self.data_type = data_type
        self.constraints = constraints or []
    
    async def validate(self, value) -> bool:
        """
        Validate the value against the field's constraints.

        Args:
            value: The value to be validated.

        Returns:
            bool: True if the value is valid, False otherwise.
        """
        for constraint in self.constraints:
            if isinstance(constraint, Rules):
                if not await constraint.validate(value):
                    return False
            elif callable(constraint):
                if not await constraint(value):
                    return False
            elif constraint == 'required' and value is None:
                return False

        return True