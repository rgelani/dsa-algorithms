# Build Tree Preorder in python
# Time Complixity :: O(n)

class BinaryTree:
    def __init__(self):
        self.idx = -1
    
    def buildTree(self, nodes):
        self.idx = self.idx + 1
          
        if(nodes[self.idx] == -1):
            return None
                 
        root = Node(nodes[self.idx])
        root.left = self.buildTree(nodes)  
        root.right = self.buildTree(nodes)
        return root
        

    # Traverse Preorder tree    
    def preorder(self, root):
        if(root is None):
            # print(-1)
            return

        print(root.data , ",")    
        self.preorder(root.left)
        self.preorder(root.right)  

    # Traverse Inorder tree   
    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        print(root.data,  ",")
        self.inorder(root.right)    

    # Traverse Postorder
    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, ",")       

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# -----------------------------
# Only runs if execute this file directly
# -----------------------------

if __name__ == "__main__": # To avoid run on import
    nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]        
    tree = BinaryTree()
    root = tree.buildTree(nodes)
    print("Tree :: ", root.data)
        
    print("Preorder Tree")  
    # root,left,right  
    tree.preorder(root) 

    print("Inorder Tree")    
    # left,root,right
    tree.inorder(root) 

    print("Postorder Tree")   
    # left,right,root 
    tree.postorder(root) 
        