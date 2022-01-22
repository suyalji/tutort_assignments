class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while temp.next:
            temp = temp.next    
        temp.next = newnode

    def print_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next     
        print("\n")    
        
    
    def delete_last_element(self):
        if self.head is None:
            print("List is empty , nothing to delete ")
            return

        temp = self.head
        
        if temp.next is None:
            temp = None
            return

        while temp.next.next:
            temp = temp.next
        temp.next = None    
        print(f"List is : ")
        self.print_list()

    def delete_first_element(self):
        if self.head is None:
            print("Nothing to delete , list is empty")
            return
        self.head = self.head.next
        return self.head
                       
                        

if __name__ == "__main__":
    l = linkedlist()
    l.append(1)
    l.append(2)        
    l.append(3)        
    l.append(4)        
    l.append(5)        
    l.append(6)        
    l.print_list()
    l.delete_last_element()
    l.delete_last_element()
    l.delete_last_element()
    l.delete_last_element()
    l.delete_last_element()
    l.delete_last_element()
    l.delete_last_element()
    l.delete_first_element()
    l.print_list()
    l.append(1)
    l.append(2)        
    l.append(3)        
    l.append(4)        
    l.append(5)        
    l.append(6)   
    l.print_list()
    l.delete_first_element()
    l.print_list()
    l.delete_first_element()
    l.print_list()
    