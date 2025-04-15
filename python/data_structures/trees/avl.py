from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class AVLNode:
    key: Any
    right: Optional['AVLNode'] = None
    left: Optional['AVLNode']  = None
    parent: Optional['AVLNode'] = None
    level: int = 0
    height: int = 0



class AVLTree:
    def __init__(self, key: Any):
        self.root = AVLNode(key)

    def insert(self, key: Any):
        node = self.__insert(key)
        self.__rebalance(node)

    def __rotate(self):
        pass

    def __rebalance(self):


    def __insert(self, key: Any) -> AVLNode:
        pass

    def __is_balanced(self, node: AVLNode | None):
        if node and node.left and node.right:
            if abs(node.left.height - node.right.height) > 1:
                return False

        elif node and node.left:
            return True

        return self.__is_balanced(node.left) and self.__is_balanced(node.right)