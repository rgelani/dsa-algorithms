# Calculate diameter of tree
# Approach 1 ::
    # d1 = Diameter of left subtree
    # d2 = Diameter of right subtree
    # d3 = Hight of left subtree + right subtree + 1
    # largest of d1, d2, d3
# time complexity :: O(N * N) // Diameter and Height

from binaryTree import BinaryTree
from height_of_tree import HeightOfNodes

class DiameterOfTree:
    def __init__(self): # optional
        pass

    def calculateDiameter(self, root):
        if root is None:
            return 0
        
        diam_left = self.calculateDiameter(root.left)
        diam_right = self.calculateDiameter(root.right)
        diam_height = HeightOfNodes.calculateHeight(root.left) + HeightOfNodes.calculateHeight(root.right) + 1

        return max(diam_height, max(diam_left, diam_right))

nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1] 
tree = BinaryTree()
root = tree.buildTree(nodes)   

diameteroftree = DiameterOfTree()
diameter = diameteroftree.calculateDiameter(root)
print(diameter)

