from typing import Any

from python.data_structures.trees.node import BinaryTreeNode


"""
Tree is a type of graph

Storing hierarchical relationships
- file system of computer
- structure of an html document

Chess
- possible moves of the rival

Searching and sorting algorithms

"""

class BinarySearchTree:
    def __init__(self):
        self.root: BinaryTreeNode | None = None

    def insert(self, key: Any):

        if self.root is None:
            self.root = BinaryTreeNode(key)

        else:
            self.__insert(key)

    def find(self, key: Any) -> BinaryTreeNode | None:
        return self.__find(self.root, key)

    def next(self, node: BinaryTreeNode) -> BinaryTreeNode | None:
        if node.right:
            return self.__left_descendant(node.right)

        else:
            return self.__right_ancestor(node)

    def search(self, key: Any) -> bool:
        node = self.find(key)
        if node.key == key:
            return True

        else:
            return False

    def range_search(self, start_key: Any, end_key: Any) -> list[BinaryTreeNode]:
        output = []
        node = self.find(start_key)

        while node and node.key <= end_key:
            if node.key >= start_key:
                output.append(node)

            node = self.next(node)

        return output

    def delete(self, node: BinaryTreeNode):
        self.__delete(node)

    def remove(self, key: Any):
        node = self.find(key)
        self.delete(node)

    @property
    def height(self) -> int:
        return self.__height(self.root)

    @property
    def size(self):
        return self.__size(self.root)

    @property
    def max(self):
        return self.__right_descendant(self.root)

    @property
    def min(self):
        return self.__left_descendant(self.root)

    def __insert(self, key: Any):

        nearest_node = self.find(key)

        if nearest_node.key < key:
            nearest_node.right = BinaryTreeNode(parent=nearest_node, key=key, level=nearest_node.level + 1)

        elif nearest_node.key > key:
            nearest_node.left = BinaryTreeNode(parent=nearest_node, key=key, level=nearest_node.level + 1)

        else:
            return

    def __find(self, node: BinaryTreeNode, key: Any) -> BinaryTreeNode | None:
        if node.key == key:
            return node

        if node.right and key > node.key:
            return self.__find(node.right, key)

        if node.left and key < node.key:
            return self.__find(node.left, key)

        return node

    def __height(self, node: BinaryTreeNode) -> int:
        left_height = 0
        right_height = 0

        if node.left:
            left_height = self.__height(node.left)

        if node.right:
            right_height = self.__height(node.right)

        return 1 + max(left_height, right_height)

    def __size(self, node: BinaryTreeNode) -> int:
        left_size = 0
        right_size = 0

        if node.left:
            left_size = self.__size(node.left)

        if node.right:
            right_size = self.__size(node.right)

        return 1 + left_size + right_size

    def __left_descendant(self, node: BinaryTreeNode) -> BinaryTreeNode:
        if node.left:
            return self.__left_descendant(node.left)

        else:
            return node

    def __right_descendant(self, node: BinaryTreeNode) -> BinaryTreeNode:
        if node.right:
            return self.__right_descendant(node.right)

        else:
            return node

    def __right_ancestor(self, node: BinaryTreeNode) -> BinaryTreeNode:
        if node.parent:
            if node.key < node.parent.key:
                return node.parent

            else:
                return self.__right_ancestor(node.parent)

        else:
            return node

    def __delete(self, node: BinaryTreeNode):
        if node.right:
            substitution = self.next(node)
            substitution.parent.left = substitution.right
            substitution.parent.left.parent = substitution.parent
            self.__substitute(node, substitution)

        elif node.left:
            self.__substitute(node, node.left)

    def __substitute(self, target_node: BinaryTreeNode, substitution_node: BinaryTreeNode):
        if target_node.parent:
            substitution_node.parent = target_node.parent

            if target_node.parent.left == target_node:
                target_node.parent.left = substitution_node


            else:
                target_node.parent.right = substitution_node

        else:
            self.root = substitution_node
