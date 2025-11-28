# Calculate height of tree
# left subtree height
# Right subtree height
# Root level (1)
# greater height + 1
#Time complexity = O(N)
 
from binaryTree import BinaryTree

class HeightOfNodes:
    def __init__(self): #optional
        pass 

    def calculateHeight(self, root):
        if root is None:
            return 0
        
        leftHeight = self.calculateHeight(root.left)
        rightHeight = self.calculateHeight(root.right)

        return max(leftHeight, rightHeight) + 1

# nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]  
nodes = [1,2,3,4,-1,-1,-1,-1,5,-1,-1]  
tree = BinaryTree()
root = tree.buildTree(nodes)

heightofnodes = HeightOfNodes()
height = heightofnodes.calculateHeight(root)
print(height)