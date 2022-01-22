class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class tree:
    def __init__(self):
        self.root = None
    
    # Simply insert 
    def insert(self,data):
        if self.root is None:
            self.root=node(data)
        else:
            self._insert(data,self.root)
    
    def _insert(self,value,cur_node):
        if value < cur_node.value:
            if cur_node.left == None:
                cur_node.left = node(value)
            else:
                self._insert(value,cur_node.left)
        elif value > cur_node.value:
            if cur_node.right == None:
                cur_node.right = node(value)
            else:
                self._insert(value,cur_node.right)
        else:
            print(f"Value {value} already in tree ")
    # Inorder 
    def print_tree_inorder(self):
        if self.root!= None:
            self._print_tree_inorder(self.root)        
        else:
            print("Empty Tree ")
    def _print_tree_inorder(self,cur_node):
        if cur_node!= None:
            self._print_tree_inorder(cur_node.left)
            print(cur_node.value)
            self._print_tree_inorder(cur_node.right)
    # Pre Order
    def print_tree_preorder(self):
        if self.root!=None:
            self._print_tree_preorder(self.root)
        else:
            print("Empty Tree ")    

    def _print_tree_preorder(self,cur_node):
        if cur_node != None:
            print(cur_node.value)
            self._print_tree_preorder(cur_node.left)
            self._print_tree_preorder(cur_node.right)
    # Post Order 
    def print_tree_postorder(self):
        if self.root != None:
            self._print_tree_postorder(self.root)
        else:
            print("Empty Tree ")    
    
    def _print_tree_postorder(self,cur_node):
        if cur_node != None:
            self._print_tree_postorder(cur_node.left)
            self._print_tree_postorder(cur_node.right)
            print(cur_node.value)        

    # height 
    def height(self):
        if self.root != None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,cur_node,cur_height):
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left,cur_height+1)
        right_height = self._height(cur_node.right, cur_height+1)
        return max(left_height,right_height)    

    # Search a value 
    def search(self,value):
        if self.root != None:
            return self._search(self.root,value)
        else:
            print("***  Empty Tree *** ")
            return None

    def _search(self,cur_node,value):
        if  cur_node.value == value:
            print("Element found ")
            return True
        elif value < cur_node.value and cur_node.left != None:        
            return self._search(cur_node.left,value)
        elif value > cur_node.value and cur_node.right != None:    
            return self._search(cur_node.right, value)
        else:    
            print("Element Not Found")
            return False


## ------------------------------------------------------------- ## 

if __name__ == "__main__":
    Tree = tree()
    while(1):
        print("1 : Insert Element ")
        print("2 : Print Pre-Order ")
        print("3 : Print Post-Order ")
        print("4 : Print In-Order ")
        print("5 : Height of the Tree ")
        print("6 : Search an element ")
        choice = int(input("Enter your choice .... "))
        if choice == 1:
            n = int(input("Enter an element"))
            Tree.insert(n)
        elif choice == 2:
            Tree.print_tree_preorder() 
        elif choice == 3:
            Tree.print_tree_postorder()
        elif choice == 4:
            Tree.print_tree_postorder() 
        elif choice == 5:
            print(f"Height of the Tree : {Tree.height()}")
        elif choice == 6:
            n = int(input("Enter the element for search"))                  
            Tree.search(n)
        else:
            exit()

## ------------------------------------------------------------ ## 
    """             


    Tree.insert(5)
    Tree.insert(5)
    Tree.insert(3)
    
    Tree.insert(8)
    Tree.insert(8)
    print("\nInorder")
    Tree.print_tree_inorder()
    print("\nPreOrder")
    Tree.print_tree_preorder()
    print("\nPost Order")
    Tree.print_tree_postorder()
    print("Height of tree : ",end = "")
    print(Tree.height())
    print("Search a value 10 ")
    Tree.search(10)
    Tree.search(5)
    Tree.search(8)
    Tree.search(3)

    """