class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def add(self,data):
        new = node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new 

    def print_list(self):
        if self.head is None:
            print("Empty list")
            return
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next    
        print("\n") 

    def count_list(self):
        if self.head is None:
            return 0
        else:
            temp = self.head
            count = 0
            while temp:
                count += 1
                temp = temp.next 
        return count        

    def print_odd(self):
        if self.head is None:
            return
        count = 1
        temp = self.head
        while temp:
            if count % 2 != 0:
                print (temp.data)
            count += 1
            temp = temp.next       
    def print_even(self):
        if self.head is None:
            return
        count = 1
        temp = self.head
        while temp:
            if count % 2 == 0:
                print (temp.data)
            count += 1
            temp = temp.next  

    def delete_last(self):
        if self.head is None:
            print("Nothing to delete")
            return
          
        temp = self.head
        if temp.next is None:
            temp = None
            return
        while temp.next.next:
              temp = temp.next
        temp.next = None      

    def delete_given_element(self,element):
        count = 0
        if self.head is None:
            return 
        temp = self.head
        if temp.data == element: # If first element 
            self.head = temp.next
            temp = None
            return
        while temp.next.data != element:
            temp = temp.next
        temp.next = temp.next.next        

    def delete_kth_element(self):
        pass

if __name__ == "__main__":
   
    my_list = linkedlist()
    my_list.print_list()        
    my_list.add(1)
    my_list.add(2)
    my_list.add(3)
        
    my_list.print_list()
    print("Length : ",my_list.count_list())                
    my_list.print_odd()
    my_list.print_even()
    print("delete last")
    my_list.delete_last()
    my_list.print_list()
    my_list.delete_given_element(1)
    my_list.print_list()
    my_list.delete_given_element(1)
    my_list.print_list()
    my_list.delete_given_element(1)
    my_list.add(11)
    my_list.add(22)
    my_list.add(33)
    my_list.print_list()
    my_list.delete_given_element(22) 
    my_list.print_list()   
