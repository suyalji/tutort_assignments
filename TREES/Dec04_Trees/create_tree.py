class node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createnode(self,data):
        return node(data)
    
    def insert_node(self,node,data):
        if node is None:
            return self.createnode(data)
        if data < node.data:
            node.left = self.insert_node(node.left,data)
        elif data > node.data:
            node.right = self.insert_node(node.right,data)
        return node

    def preorder_traversal(self,root):
        if root is not None:
            print(root.data,end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)
                 
        

    def inorder_traversal(self,root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data,end=" " )
            self.inorder_traversal(root.right)

        

    def postorder_traversal(self,root):
        if root is not None:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data,end=" ")
        


# Driver
if __name__ == "__main__":
    tree = Tree()
    root = tree.createnode(5)     
    ##print(root.data)
    tree.insert_node(root, 2)
    tree.insert_node(root, 10)
    tree.insert_node(root, 7)
    tree.insert_node(root, 6)
    tree.insert_node(root, 15)
    tree.insert_node(root, 12)
    tree.insert_node(root, 20)
    tree.insert_node(root, 30)  
    print("\nPre-order Traverasal")             
    tree.preorder_traversal(root)
    print("\nInorder Traversal")
    tree.inorder_traversal(root)
    print("\nPost Order Traversal")
    tree.postorder_traversal(root)