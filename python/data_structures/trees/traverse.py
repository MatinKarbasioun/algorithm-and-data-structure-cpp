"""

Tree traversal:
1- depth-first traversal: completely traverse one sub-tree before exploring a sibling sub-tree.
2- breadth first traversal: traverse all nodes at one level before processing to the next level

"""



class TreeTraverse:

    def in_order_traversal(self, tree):
        if not tree:
            return

        self.in_order_traversal(tree.left)
        print(tree.key)
        self.in_order_traversal(tree.right)


    def breadth_first(self):
        return None

