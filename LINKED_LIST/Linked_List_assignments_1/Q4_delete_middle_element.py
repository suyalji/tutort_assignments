"""Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
"""
class node:
    def __init__(self,data):
        self.data = data
        self.next = None   

class linked_list:
    def __init__(self):
        self.head = None

    def insert_node(self,value):
        newnode = node(value)
        if self.head is None:
            self.head = newnode
            return 
        temp = self.head
        while temp.next:
            temp=temp.next
        temp.next = newnode
    
    def print_list(self):
        if self.head is None:
            print("**** Linked List is Empty **** ")
            return 
        temp = self.head
        print("{ ",end=" ")
        while temp:
            print(temp.data,end=" -> ") 
            temp = temp.next
        print("} \n") 

    def delete_middle_element(self):
        if self.head is None:
            print("Empty Listv ")
            return
        
        if self.head.next is None: # if only one node 
            self.head = None
            return
        
        len = self.find_length()
        if len%2 == 0 :
            middle = int(len/2)+1
        else:
            middle = int((len+1)/2)    

        print(f"Length : {len} , middle_pos : {middle}") 
        temp = self.head 
        count = 2
        while temp.next and (count < middle):
              temp = temp.next 
              count += 1

        print(f"middle element : {temp.next.data}")

        temp2 = temp.next
        temp.next = temp2.next
        temp2 = None   

