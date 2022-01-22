"""
Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, 
and return the new head.
"""

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def insert_node(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        return self.head

    def print_list(self):
        if self.head is None:
            print("No elements in the linked list ")
            return            
        temp = self.head
        while temp:
            print(temp.data,end=" => " )
            temp = temp.next
        print("\n")    
    
    def remove_first(self):
        if self.head is None:
            print("\n*** Linked List is empty *** ")
            return
        temp = self.head    
        self.head = self.head.next
        temp = None
        return self.head    

    def remove_last(self):
        if self.head is None:
            print("\n*** Linked List is empty *** ")
            return
        if self.head.next is None:
            self.head = None
            return None

        temp = self.head
        
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        return self.head

    def remove_given_node(self,val):
        cur_node = self.head
        
        # Case 1 : If the node to be deleted in Head Node
        if cur_node and cur_node.data == val:
            print("The Node to be deleted is Head Node ... ")
            self.head = cur_node.next
            cur_node = None
            return 
        
        # Case 2 : If the Node to be deleted is other than Head Node
        prev_node = None
        while cur_node and cur_node.data != val:
            prev_node = cur_node
            cur_node = cur_node.next
        
        # Value Not present in the List 
        if cur_node is None:
            print("Element is Not found in the list  ")
            return self.head    

        prev_node.next = cur_node.next
        cur_node = None
        
        return self.head

    def delete_node_with_pos(self,pos):
        curr = self.head
        if pos == 1:
            self.head = curr.next
            curr = None
            return self.head          
        curr = self.head
        prev = None
        count = 2
        while curr and count != val :
            prev = curr
            curr = curr.next
            count += 1

        prev.next = curr.next
        curr = None    
        return self.head
 

          





if __name__ == "__main__":
      
       root = linked_list()

       while(1):
            
            print("\n**************************************")
            print("1 : Show List")
            print("2 : Insert and show  ")
            print("3 : Delete from Front  ")
            print("4 : Delete from Last ")
            print("5 : Remove given node ")
            print("6 : Remove as per location ")
            print("0 : Exit")
            print("**************************************")
            n = int(input("Enter your choice ")) 
            if n == 1:
                root.print_list()
            elif n == 2:
                value = input("Enter new node value ")   
                root.insert_node(value)
                root.print_list()
            elif n == 3:
                root.remove_first()
                root.print_list()
            elif n == 4:
                root.remove_last()
                root.print_list()        
            elif n == 5:
                val = input("Enter the node value to be removed ")
                root.remove_given_node(val)
                root.print_list()    
            elif n == 6:
                val = int(input("Enter the position"))
                root.delete_node_with_pos(val)
                root.print_list()
            else:
                exit()

