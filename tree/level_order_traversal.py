#Traverse binary tree and print levels
# Queue - FIFO,
# Iteration,
# BFS - Breadth First Search

from binaryTree import BinaryTree
from collections import deque

class LevelOrderTraverse:
    def __init__(self, root):
        self.root = root

    def traverse(self):
        if not self.root:
            return
        q = deque()
        q.append(self.root)
        q.append(None) # level marker

        while q:
            currentNode = q.popleft()
            if currentNode is None:
                print() # new line for next level
                if q: # add new marker only if nodes remain
                    q.append(None)
                continue

            print(currentNode.data, end=" ")  

            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)    

nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]        
tree = BinaryTree()
root = tree.buildTree(nodes)
level = LevelOrderTraverse(root)
level.traverse()

