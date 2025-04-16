from dataclasses import dataclass
from typing import Any


"""
level is: num of edges between root and node + 1
"""


@dataclass
class BinaryTreeNode:
    key: Any
    level: int = 0
    parent: 'BinaryTreeNode' | None = None
    left: 'BinaryTreeNode' | None = None
    right: 'BinaryTreeNode' | None = None

    @property
    def is_leaf(self):
        return not self.left and not self.right

    @property
    def sibling(self) -> None:
        return [self.left, self.right] if self.left and self.right else None
