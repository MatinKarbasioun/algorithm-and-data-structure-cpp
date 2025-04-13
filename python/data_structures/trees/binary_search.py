from typing import Any

from python.data_structures.trees.node import BinaryTreeNode


class BinarySearchTree:
    def __init__(self):
        self.root: BinaryTreeNode | None = None

    def insert(self, key: Any):
        if self.root is None:
            self.root = BinaryTreeNode(key)

        else:
            self.root.add_node(BinaryTreeNode(key))

    def find(self, key: Any) -> BinaryTreeNode | None:
        if self.root is None:
            return None

        return self.root.find(key)

    def next_max(self, key: Any) -> BinaryTreeNode | None:
        node = self.find(key)

        if node:
            if node.right:
                return node.right.min()

            else:
                return None

    def next_min(self, key: Any) -> BinaryTreeNode | None:
        node = self.find(key)

        if node:
            if node.left:
                return node.left.max()

            else:
                return None

    def max(self):
        return self.root.max()

    def min(self):
        return self.root.min()

    def search(self, start_key: Any, end_key: Any):
        pass

    def delete(self, key: Any):
        pass
