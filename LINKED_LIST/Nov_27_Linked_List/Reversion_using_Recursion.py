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

    """ RECURSIVE NOT WORKING YET FOR ME 
    def reverse_recursive(self):
        if self.head is None:
            return
        newhead = self.head
        if self.head.next:
            self.head = self.head.next
            newhead = self.reverse_recursive()
            self.head.next.next = self.head 
        self.head.next = None
        return newhead            
    """
if __name__ == "__main__":
    l = linkedlist()
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.print_list()
    
    print("Reverse the list recursively")
    l.reverse_recursive()
    l.print_list()
