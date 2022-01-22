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
           return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode
        return self.head

    def insert_at_first(self,value):
        newnode = node(value)
        if self.head is None:
            self.head = newnode
            return
        else:
           temp = self.head
           newnode.next = temp
           self.head = newnode
        return self.head 

    def display(self):
        if self.head is None:
            print("Empty List ") 
            return 

        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("\n")

    def count(self):
        count = 0 
        if self.head is None:
            return 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count 

    def delete_m_after_n(self,m,n):
        if self.head is None:
            print("Nothing to delete ")
            return
            
        list_length = self.count()
        if list_length < m+n:
            print(f"Can't delete {m} nodes after {n} nodes ")    
            return 

        c = 1 
        temp = self.head 
        while c < n :
            c += 1   
            temp = temp.next
        print(f"debug : c : {temp.data}: {c}")    
        c = 0
        while c < m:
            temp2 = temp.next
            temp.next = temp2.next
            temp2 = None
            c += 1
        return self.head



if __name__ == "__main__":
    head = linked_list()
    head.display()
    head.insert_at_first(1)
    head.display()
    head.insert_at_first(2)                       
    head.display()
    head.insert_at_last(4)
    head.display()
    print(f"Count : {head.count()}")
    head.insert_at_first(5)    
    head.insert_at_first(6)    
    head.insert_at_first(7)    
    head.insert_at_first(8)    
    head.insert_at_first(9)
    head.display()
    print("Deleting 2 nodes after 3 nodes .... ")
    head.delete_m_after_n(2, 3)
    head.display()    
