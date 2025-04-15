import matplotlib.pyplot as plt

from python.data_structures.trees.node import BinaryTreeNode


class TreeVisualizer:
    def __init__(self, root):
        self.root = root
        self.positions = {}
        self.levels = {}

    def _compute_positions(self, node: BinaryTreeNode, x=0, y=0, level=0):
        if node:
            if level not in self.levels:
                self.levels[level] = []
            self.levels[level].append(node)

            self._compute_positions(node.left, x - 2 ** (-level - 1), y - 1, level + 1)
            self.positions[node] = (x, y)
            self._compute_positions(node.right, x + 2 ** (-level - 1), y - 1, level + 1)

    def draw(self):
        self._compute_positions(self.root)
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.axis('off')

        for node, (x, y) in self.positions.items():
            ax.text(x, y, str(node.key), ha='center', va='center',
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='lightblue'))

            if node.left:
                x0, y0 = self.positions[node]
                x1, y1 = self.positions[node.left]
                ax.plot([x0, x1], [y0, y1], 'k-')

            if node.right:
                x0, y0 = self.positions[node]
                x1, y1 = self.positions[node.right]
                ax.plot([x0, x1], [y0, y1], 'k-')

        plt.show()