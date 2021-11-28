class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def print_list(self):
        if not self.head:
            print("Empty list")
            return
        temp = self.head    
        while temp:
            print (temp.data,end=" -> ")
            temp = temp.next
        print("\n")

    def middle(self):
        if not self.head:
            print("Empty list")
            return
        elif self.head.next.next == None:
            print("only two elements")    
            return
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)        

if __name__ == "__main__":
   
    my_list = linkedlist()
    my_list.print_list()        
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
   
       
    my_list.print_list()
    my_list.middle()    

