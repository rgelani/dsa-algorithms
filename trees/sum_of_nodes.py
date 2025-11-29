# Calculate sum of nodes
# left subtree sum + right subtree sum + root
# Time Complexity = O(N)

from binaryTree import BinaryTree

class SumOfNodes:
    def __init__(self): # optional
        pass

    def calculateSum(self, root):
        if root == None:
            return 0
        
        leftSum = self.calculateSum(root.left)
        rightSum = self.calculateSum(root.right)

        return leftSum + rightSum + root.data

nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]  
tree = BinaryTree()
root = tree.buildTree(nodes)

sumofnodes = SumOfNodes()
sum = sumofnodes.calculateSum(root)
print(sum)