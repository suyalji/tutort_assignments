class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        new = node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new

    def print_list(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.data,end = "  ")
            temp = temp.next
        print("\n")

    def reverse_iterative(self):
        if self.head is None:
            return
        curr = self.head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        self.head = prev
        return self.head                  

if __name__ == "__main__":
    l = linkedlist()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.print_list()
    print("Reverse the list ")
    l.reverse_iterative()
    l.print_list()
