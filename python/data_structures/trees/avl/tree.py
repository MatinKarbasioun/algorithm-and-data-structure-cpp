from dataclasses import dataclass
from typing import Any, Optional, Tuple

"""

Height: the maximum depth of its subtree

Condition (balance condition) --> |left.height - right.height| <= 1 for each node

Left - heavy --> 
1- rotate right or
2- rotate left-right

right - heavy -->
1- rotate left or
2- rotate right-left

try to put a sub-tree to the node that it has not enough sub-tree

"""

from .node import AVLNode



class AVLTree:
    def __init__(self, key: Any):
        self.root = AVLNode(key)

    def insert(self, key: Any):
        node = self.__insert(key)
        self.__rebalance(node)

    def insert_node(self, node: AVLNode):
        self.insert_node(self.root, node)

    def next(self, node: AVLNode) -> AVLNode | None:
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

    def range_search(self, start_key: Any, end_key: Any) -> list[AVLNode]:
        output = []
        node = self.find(start_key)

        while node and node.key <= end_key:
            if node.key >= start_key:
                output.append(node)

            node = self.next(node)

        return output

    def delete(self, node: AVLNode):
        substitution_node = self.__delete(node)

        if substitution_node:
            parent = substitution_node.parent

            if parent:
                self.__rebalance(parent)

    def remove(self, key: Any):
        node = self.find(key)
        self.delete(node)

    @classmethod
    def merge(cls, smaller_tree: 'AVLTree', larger_tree: 'AVLTree') -> 'AVLTree':
        """
        merge when applicable that the one of both tree with its root and keys are smaller than another one
        :param smaller_tree: it should be the tree which its nodes' key are smaller than larger_tree tree
        :param larger_tree: it should be the tree which its nodes' key are bigger than smaller_tree tree
        :return: a new merged tree with AVL properties
        """

        node = smaller_tree.max
        smaller_tree.delete(node)
        new_tree = cls(node.key)

        cls.avl_tree_merge_with_roots(larger_tree.root, smaller_tree.root, new_tree)
        return new_tree

    @classmethod
    def avl_tree_merge_with_roots(cls, bigger_node, smaller_node, tree):
        if abs(bigger_node.height - smaller_node.height) <= 1:
            cls.merge_with_roots(bigger_node, smaller_node, tree)
            tree.root.height = max(bigger_node.height, smaller_node.height)
            return tree

        elif smaller_node.height > bigger_node.height:
            new_node = cls.avl_tree_merge_with_roots(smaller_node.right, bigger_node, tree)
            smaller_node.right = new_node
            new_node.parent = smaller_node
            # rebalance node (smaller_node)

            return tree

        else:
            new_node = cls.avl_tree_merge_with_roots(bigger_node.left, smaller_node, tree)
            bigger_node.left = new_node
            new_node.parent = bigger_node
            # rebalance node (smaller_node)

            return tree


    @classmethod
    def merge_with_roots(cls, bigger_root, smaller_root, tree):
        tree.root.left = smaller_root
        tree.root.right = bigger_root
        smaller_root.parent = tree.root
        bigger_root.parent = tree.root
        return tree

    def split(self, key: Any) -> Tuple[AVLNode | None, AVLNode | None]:
        if not self.root:
            return None, None

        return self.__split(self.root, key)


    def __split(self, node: 'AVLNode', key: Any) -> Tuple[AVLNode | None, AVLNode | None]:
        if not node:
            return None, None

        if key < node.key:
            new_tree = AVLTree(node.key)
            first_root, second_root = self.__split(node.left, key)
            new_root = self.merge_with_roots(second_root, node.right, new_tree)
            return first_root, new_root

        if key >= node.key:
            new_tree = AVLTree(node.key)
            first_root, second_root = self.__split(node.right, key)
            new_root = self.merge_with_roots(first_root, node.left, new_tree)
            return new_root, second_root

    @property
    def height(self) -> int:
        return self.root.height

    @property
    def size(self):
        return self.__size(self.root)

    @property
    def max(self):
        return self.__right_descendant(self.root)

    @property
    def min(self):
        return self.__left_descendant(self.root)

    def __insert(self, key: Any) -> AVLNode:

        nearest_node = self.find(key)

        if not nearest_node:
            self.root = AVLNode(key)
            return self.root

        if nearest_node.key < key:
            nearest_node.right = AVLNode(parent=nearest_node, key=key, level=nearest_node.level + 1)
            nearest_node.add_height(1)

        elif nearest_node.key > key:
            nearest_node.left = AVLNode(parent=nearest_node, key=key, level=nearest_node.level + 1)
            nearest_node.add_height(1)

        else:
            return nearest_node

    def insert_node(self, parent_node: AVLNode, node: AVLNode) -> AVLNode:

        nearest_node = self.__find(parent_node, node.key)

        if nearest_node.key <= node.key:
            nearest_node.right = node

        elif nearest_node.key > node.key:
            nearest_node.left = node

        return nearest_node

    def find(self, key: Any) -> AVLNode | None:
        return self.__find(self.root, key)

    def __rebalance(self, rebalance_node: AVLNode):
        parent = rebalance_node.parent

        if rebalance_node.left.height > rebalance_node.right.height + 1:
            self.__rebalance_right(rebalance_node)

        if rebalance_node.right.height > rebalance_node.left.height + 1:
            self.__rebalance_left(rebalance_node.left)

        self.__adjust_height(rebalance_node)

        if parent:
            self.__rebalance(parent)

    def __rebalance_right(self, node: AVLNode):
        left_node = node.left

        left_height = 0
        right_height = 0

        if left_node.left: left_height = left_node.left.height
        if left_node.right: right_height = left_node.right.height

        if right_height > left_height:
            self.__rotate_left(left_node)

        self.__rotate_right(node)

    def __rebalance_left(self, node: AVLNode):
        right_node = node.right

        left_height = 0
        right_height = 0

        if right_node.left: left_height = right_node.left.height
        if right_node.right: right_height = right_node.right.height

        if left_height > right_height:
            self.__rotate_right(right_node)

        self.__rotate_left(node)

    def __rotate_right(self, node: AVLNode):
        new_root = node.right
        left_subtree = new_root.left
        new_root.parent = node.parent
        node.parent = new_root
        new_root.right = node
        self.insert_node(node, left_subtree)

    def __rotate_left(self, node: AVLNode):
        new_root = node.left
        right_subtree = new_root.right
        new_root.parent = node.parent
        node.parent = new_root
        new_root.left = node
        self.insert_node(node, right_subtree)

    def __adjust_height(self, node: AVLNode) -> int:
        left_height = 0
        right_height = 0

        if node.left:
            left_height = self.__adjust_height(node.left)

        if node.right:
            right_height = self.__adjust_height(node.right)

        node.height = 1 + max(left_height, right_height)
        return node.height

    def __size(self, node: AVLNode) -> int:
        left_size = 0
        right_size = 0

        if node.left:
            left_size = self.__size(node.left)

        if node.right:
            right_size = self.__size(node.right)

        return 1 + left_size + right_size

    def __find(self, node: AVLNode, key: Any) -> AVLNode | None:
        if node.key == key:
            return node

        if node.right and key > node.key:
            return self.__find(node.right, key)

        if node.left and key < node.key:
            return self.__find(node.left, key)

        return node

    def __left_descendant(self, node: AVLNode) -> AVLNode:
        if node.left:
            return self.__left_descendant(node.left)

        else:
            return node

    def __right_descendant(self, node: AVLNode) -> AVLNode:
        if node.right:
            return self.__right_descendant(node.right)

        else:
            return node

    def __right_ancestor(self, node: AVLNode) -> AVLNode:
        if node.parent:
            if node.key < node.parent.key:
                return node.parent

            else:
                return self.__right_ancestor(node.parent)

        else:
            return node

    def __delete(self, node: AVLNode) -> AVLNode:
        substitution = None

        if node.right:
            substitution = self.next(node)

            if substitution.parent.left == substitution:
                substitution.parent.left = None

            else:
                substitution.parent.right = None

            substitution.parent.decrease_height()
            substitution.height = node.height - 1 if node.height > 1 else 1
            substitution.parent.left = substitution.right
            substitution.parent.left.parent = substitution.parent
            substitution.height = node.height
            self.__substitute(node, substitution)

        elif node.left:
            substitution = node.left
            self.__substitute(node, substitution)

        return substitution

    def __substitute(self, target_node: AVLNode, substitution_node: AVLNode):
        if target_node.parent:
            substitution_node.parent = target_node.parent
            if target_node.parent.left == target_node:
                target_node.parent.left = substitution_node


            else:
                target_node.parent.right = substitution_node

        else:
            self.root = substitution_node

    def is_avl(self):
        self.__is_balanced(self.root)

    @classmethod
    def __is_balanced(cls, node: AVLNode | None) -> bool:
        right_height = 0
        left_height = 0

        if node.left: left_height = node.height
        if node.right: right_height = node.height
        return abs(left_height - right_height) <= 1