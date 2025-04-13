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

    def add_node(self, key: Any) -> None:
        if key is None:
            return

        if key > self.key:
            self.right.add_node(key) if self.right else self.right = BinaryTreeNode(parent=self,
                                                                                    key=key,
                                                                                    level=self.level + 1)



        elif key < self.key:
            self.left.add_node(key) if self.left else self.left = BinaryTreeNode(parent=self,
                                                                                 key=key,
                                                                                 level=self.level + 1)

        else:
            return

    def find(self, key: Any) -> 'BinaryTreeNode':

        if self.right and key > self.key:
            return self.right.find(key)

        if self.left and key < self.key:
            return self.left.find(key)

        return self

    def max(self):
        if self.right:
            return self.right.max()

        else:
            return self

    def min(self):
        if self.left:
            return self.left.min()

        else:
            return self

    def next_max(self):
        if self.right:
            return self.right.next_max()

    def height(self) -> int:
        left_height = 0
        right_height = 0

        if self.left:
            left_height = self.left.height()

        if self.right:
            right_height = self.right.height()

        return 1 + max(left_height, right_height)

    def size(self):
        left_size = 0
        right_size = 0

        if self.left:
            left_size = self.left.size()

        if self.right:
            right_size = self.right.size()

        return 1 + left_size + right_size

    @property
    def is_lead(self):
        return not self.left and not self.right

    @property
    def sibling(self) -> None:
        return [self.left, self.right] if self.left and self.right else None

    @property
    def parent(self):
        return self.parent