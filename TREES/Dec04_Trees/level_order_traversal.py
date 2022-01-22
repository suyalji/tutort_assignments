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

    def inorder_traversal(self,root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(root.data,end=" ")
            self.inorder_traversal(root.right)


# Driver 
if __name__ == "__main__":
    tree = Tree()
    root = tree.createnode(5)
    tree.insert_node(root, 2)
    tree.insert_node(root,6 )
    tree.insert_node(root,7)
    tree.inorder_traversal(root)                   

