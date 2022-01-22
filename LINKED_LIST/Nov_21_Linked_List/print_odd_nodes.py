class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked:
    def __init__(self):
        self.head = None

    def append(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = newnode

    def print_list(self):
        if self.head is None:
            print('List is empty')
            return
        temp = self.head
        while(temp):
            print(temp.data,end="->")
            temp=temp.next
         
    def print_odd(self):
        if self.head is None:
            return
        temp = self.head
        count = 1
        while(temp):
            if count%2 != 0:
                print(temp.data)
                temp = temp.next
            else:
                temp = temp.next 
            count += 1           
    def print_even(self):
        if self.head is None:
            return
        temp = self.head
        count = 1
        while(temp):
            if count%2 == 0:
                print(temp.data)
                temp = temp.next
            else:
                temp = temp.next 
            count += 1           

    

if __name__ == "__main__":
    mylist = linked()
    mylist.print_list()
    mylist.append(7)
    mylist.append(9)
    mylist.append(10)
    mylist.print_list()
    print("Print odd..")
    mylist.print_odd()
    print("print even..")
    mylist.print_even()
                                