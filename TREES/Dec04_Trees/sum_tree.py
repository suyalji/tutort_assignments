class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def createnode(self,data):
        return node(data)

    def insert_node(self,node,data):
        if node is None:
            return self.createnode(data)
        if data < node.data:
            node.left = self.insert_node(node.left, data)     
        elif data > node.data:
            node.right = self.insert_node(node.right, data)
        return node 

    def preorder_traversal(self,node):
        if node is not None:
            print(node.data,end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def sumtree(self,node):
        if node is None:
            return 0
        left_sum  =  self.sumtree(node.left)
        right_sum =  self.sumtree(node.right)
        root.data = left_sum + right_sum + root.data
        print(root.data)
        return node.data


# Driver 
if __name__ == "__main__":
    tree = Tree()
    root = tree.createnode(1)
    tree.insert_node(root,2)
    tree.insert_node(root,4)
    tree.insert_node(root,5)
    tree.insert_node(root,3)
    tree.insert_node(root,6)
    tree.insert_node(root,7)
    tree.insert_node(root,9)

    tree.preorder_traversal(root)
    print("\nSumTree\n")
    tree.sumtree(root)
    print("\n\n")
    tree.preorder_traversal(tree.sumtree(root))