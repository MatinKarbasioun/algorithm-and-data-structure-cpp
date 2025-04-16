from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class AVLNode:
    key: Any
    right: Optional['AVLNode'] = None
    left: Optional['AVLNode']  = None
    parent: Optional['AVLNode'] = None
    level: int = 0
    height: int = 0

    def add_height(self, child_height):
        self.height = max(child_height + 1, self.height)
        if self.height: self.parent.add_height(self.height)

    def decrease_height(self):
        right_height = 0
        left_height = 0

        if self.left:
            left_height = self.left.height

        else:
            right_height = self.left.height

        self.height = 1 + max(left_height, right_height)

        if self.parent: self.parent.decrease_height()
