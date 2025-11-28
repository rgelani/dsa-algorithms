# Counts total number of nodes in tree

from binaryTree import BinaryTree

class CountNodes:
    def __init__(self):
        pass

    def countOfNodes(self, root):
        if root == None:
            return 0
        
        leftCount = self.countOfNodes(root.left)
        rightCount = self.countOfNodes(root.right)

        return leftCount + rightCount + 1

nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1] 
tree = BinaryTree()
root = tree.buildTree(nodes)

countNode = CountNodes()
total_node = countNode.countOfNodes(root)
print(total_node)