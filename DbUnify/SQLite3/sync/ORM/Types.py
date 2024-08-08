from .Field import Field
from typing import List, Optional

class IntegerField(Field):
    def __init__(self, constraints: Optional[List[str]] = None):
        super().__init__('INTEGER', constraints)

class TextField(Field):
    def __init__(self, constraints: Optional[List[str]] = None):
        super().__init__('TEXT', constraints)
