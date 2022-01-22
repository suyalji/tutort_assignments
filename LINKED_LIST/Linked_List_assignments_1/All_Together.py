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

    def find_length(self):
        if self.head is None:
            return 0
        count = 0    
        temp = self.head    
        while temp:
            count += 1
            temp = temp.next
        return count        
    
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
      
    def remove_all_given_elements(self,value):
        if self.head is None:
            print("Empty list")
            return
        
        temp = self.head
        prev = None

        # If head node itself contains the value or multiple occurances   
        # 1->1->1->1->2->3->4  => 2->3->4
        while temp and temp.data == value:
              self.head = temp.next
              temp = self.head

        while temp:
            while temp and temp.data != value: # iterate till the value node is found 
                prev = temp
                temp = prev.next 
            
            if temp is None:  # if nothing found & reaches to last
                return self.head     

            # actual deletion or rather link shifting  
            prev.next = temp.next
            temp = prev.next 
        
        return self.head         

    def delete_without_given_node(self,given_node):
        temp = given_node
        prev = None
        while temp.next:
            temp2 = temp.data
            temp.data = temp.next.data
            temp.next.data = temp2
            temp = temp.next
        prev.next = None
        
    def delete_without_given_node_2(self,node):               
        node.data = node.next.data
        node.next = node.next.next






if __name__ == "__main__":
    root = linked_list()
    while(1):
        print("1 : Insert new node at the end ")
        print("2 : Display the List ")
        print("3 : Delete nth Node from end (Q1) ")
        print("4 : Delete middle element ")
        print("5 : Remove all occurance of given element ")
        print("0: Exit ")
        n = int(input("Enter your choice : "))
        if n == 1:
            value = int(input("Enter the node value "))
            root.insert_node(value)
            root.print_list()
        elif n == 2:
            root.print_list()
        elif n == 3: 
            value = int(input("Enter the position from end "))
            root.delete_nth_node_from_end(value)
            root.print_list()    
        elif n == 4:
            root.delete_middle_element()
            root.print_list()
        elif n == 5:
            value = int(input("Enter the value "))
            root.remove_all_given_elements(value)
            root.print_list()
                  
        else:
            exit()        




