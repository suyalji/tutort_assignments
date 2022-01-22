"""
Given the head of a linked list, remove the nth node from 
the end of the list and return its head.
"""
class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
    
    def insert_at_last(self,value):
        newnode = node(value)
        
        if self.head is None:
            self.head = newnode
            return self.head
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        return self.head

    def print_list(self):
        if self.head is None:
            print("\n**** Linked List is Empty **** \n")
            return
        temp = self.head
        print("{ ",end=" ")
        while temp:
            print(temp.data,end=" -> ")
            temp = temp.next
        print(" } \n")

    def insert_at_first(self,value):
        newnode = node(value)
        newnode.next = self.head
        self.head = newnode 
        return self.head

    def insert_at_position(self,value,position):
        newnode = node(value)
        if position == 1:
            newnode.next = self.head
            self.head = newnode
        count = 2
        temp = self.head
        while temp.next and (count - position != 1):
            temp=temp.next
            count += 1
        temp2 = temp.next    
        temp.next = newnode
        newnode.next = temp2    

    def insert_at_middle(self,value):
        newnode = node(value)
        if self.head is None:
            print("Linked is empty")
            self.head = newnode
            return
        temp = self.head
        count = 0
        while temp:  # find length 
            count+=1
            temp = temp.next
        middle = count/2
        counter = 1
        temp = self.head
        while counter < middle: # navigate to middle 
              temp = temp.next
              counter += 1
        temp3 = temp.next
        temp.next = newnode
        newnode.next = temp3

    def delete_first_element(self):
        if self.head is None:
            print("Linked list is empty ")
            return                
        temp = self.head       
        self.head = temp.next 
        temp = None

    def delete_last_element(self):
        if self.head is None:
            print("*** Linked list is empty *** ")
            return
        if self.head.next is None: # list has only 1 element 
            self.head = None
            return None

        temp = self.head
        
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        return self.head

    def find_length(self):
        if self.head is None:
            return 0
        count = 0    
        temp = self.head    
        while temp:
            count += 1
            temp = temp.next
        return count

    def delete_at_position(self,position):
        if self.head is None:
            print("Empty Linked list ")
            return 
        if position > self.find_length():
            print("!!! Incorrect position !!! ")
            return 

        if position == 1 : # first element 
           temp = self.head
           self.head = temp.next
           temp = None
           return 
        temp = self.head 
        count = 2
        while temp.next.next and count < position :
            temp = temp.next
            count += 1
        temp2 = temp.next
        temp.next = temp2.next
        temp2 = None   
            
    def delete_nth_node_from_end(self,n):
        if self.head is None:
            print("Linked list empty ")
            return 
        len = self.find_length()    
        if n > len:
            print("Position is wrong ")
            return 
        
        position = len - n + 1

        if position == 1 : # first node 
            temp = self.head
            self.head = temp.next
            temp = None
            return 
        temp = self.head 
        count = 2
        while temp.next.next and count < position:
            temp = temp.next
            count += 1
        temp2 = temp.next
        temp.next = temp2.next
        temp2 = None             
    
    def delete_nth_node_from_end_2(self,value):
        if self.head is None:
            print("Empty List")
            return 
        len = self.find_length()    
        start = 1
        last = value
        if start == last: # First Node
            temp = self.head
            self.head = temp.next
            temp = None
            return 

        temp = self.head     
        while last < len-1:
            temp = temp.next
            start =+ 1
            last += 1
        pass

    def delete_node_with_value(self,value):
        if self.head is None :
            print("Empty List ")
            return 

        if self.head.data == value :  # First Node 
            temp = self.head
            self.head = temp.next
            temp = None
            return 
     
        temp = self.head 
        
        while temp.next and temp.next.data != value:
            temp = temp.next 
        
        if not temp.next :
            print("Value Not Found ")
            return 
        else:    
            temp2 = temp.next
            temp.next = temp2.next
            temp2 = None 


        












    # driver 
if __name__ == "__main__":
    root = linked_list()
    while(1):
        print("1 : insert_node_at_first")
        print("2 : insert_node_at_last")
        print("3 : insert at given position ")
        print("4 : Insert at middle ")
        print("5 : Delete first element")
        print("6 : Delete last element ")
        print("7 : Delete at a Position ")
        print("8 : Delete nth node from end ")
        print("9 : Delete node with given value ")
        print("99 : Print the List ")
        print("0 : Exit")
        n = int(input("Enter your choice .. "))
        if n == 1:
            value = int(input("Enter the node value : "))
            root.insert_at_first(value)
            root.print_list()
        elif n == 2:
            value = int(input("Enter the node value : "))
            root.insert_at_last(value)
            root.print_list()
        elif n == 3 :
             value = int(input("Enter the value : "))
             position = int(input("Enter the position : "))
             root.insert_at_position(value, position)
             root.print_list()
        elif n == 4:
            value = int(input("Enter the value : "))
            root.insert_at_middle(value)
            root.print_list()
        elif n == 5:
            root.delete_first_element()
            root.print_list()
        elif n == 6:
            root.delete_last_element()
            root.print_list()    
        elif n == 7 :
            position = int(input("Enter the position "))
            root.delete_at_position(position)    
            root.print_list()
        elif n == 8 :
            position = int(input("Enter position from end "))
            root.delete_nth_node_from_end(position)
            root.print_list()
        elif n == 9 :
            value = int(input("Enter the Node value to be deleted :  "))    
            root.delete_node_with_value(value)
            root.print_list()
        elif n == 99 :
            root.print_list()    
        else:
            exit()

                  

