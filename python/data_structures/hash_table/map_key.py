from dataclasses import dataclass
from typing import AnyStr, Any


@dataclass
class MapKey:
    key: Any
    value: Any

    def __eq__(self, key: str):
        if self.key == key:
            return True

        else:
            return False