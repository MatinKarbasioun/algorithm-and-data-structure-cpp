from __future__ import annotations

from typing import Any

from dataclasses import dataclass



@dataclass
class Node:
    key: Any
    next_pointer: Node | None = None
    previous_pointer: Node | None = None

    def top_back(self) -> Any:
        if self.next_pointer:
            return self.next_pointer.top_back()

        else:
            return self.key

    def push_back(self, node: Node):
        if self.next_pointer is None:
            self.next_pointer = node

        else:
            self.next_pointer.push_back(node)

    def find(self, key: Any) -> bool:
        if self.key == key:
            return True

        elif self.next_pointer:
            return self.next_pointer.find(key)

        else:
            return False
