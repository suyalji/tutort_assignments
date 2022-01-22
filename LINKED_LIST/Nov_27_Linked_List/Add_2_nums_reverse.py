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
        while temp.next:
            temp = temp.next
        temp.next = newnode

    def print_list(self):
        if self.head is None:
            print ("list is empty")
            return
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    lst = linked()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.print_list() 



