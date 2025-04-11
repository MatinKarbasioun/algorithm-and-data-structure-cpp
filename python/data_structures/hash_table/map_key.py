from dataclasses import dataclass
from typing import AnyStr, Any


@dataclass
class MapKey:
    key: Any
    value: Any

    def __eq__(self, other):
        if self.key == other.key:
            return True
