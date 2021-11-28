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
            return 
        temp = self.head
        while temp:
            print(temp.data,end = " ")
            temp = temp.next
        print("\n")    

    def delete_kth(self,k):  ## yet to complete
        if self.head is None:
            return
        count = 1
        if k == 1:
            self.head = self.head.next
            return self.head
        temp = self.head    
        while temp:
            count += 1
            if k - count == 1:
                d = temp.next
                temp.next = temp.next.next
                return
            temp = temp.next    
        pass    

    def delete_kth_from_end(self,k):
        pass 
                
   

if __name__ == "__main__":
    l = linkedlist()
    l.append(1)
    l.append(2)
    l.append(3)
    l.print_list()
    l.delete_kth(2)
    l.print_list()