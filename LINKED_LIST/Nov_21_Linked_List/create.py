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
        else:    
            temp = self.head
            while temp.next != None:
                temp=temp.next
            temp.next = new_node      
    
    def prepand(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def traverse(self):
        temp = self.head    
        while temp:
            print (temp.data,end=" -> ")
            temp = temp.next

    def insert_after_node(self, prev_node, data):
        if not prev_node: 
            print("The previous node is not in list ")
            return
        new_node = node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def count_nodes(self):
        if self.head is None:
            return 0
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next 
        return count       

    def middle_element(self):
        c = self.count_nodes()
        if c%2 == 0:
            middle = (c)/2
        else:
            middle = c+1/2 
        count = 1
        print(f"middle : {middle} , length : {c}")
        temp = self.head
        while temp:
                count += 1
                temp = temp.next
                if count == middle:
                    return temp.data      
            
      
if __name__ == "__main__":
    my_list = linkedlist()
    my_list.append(1)
    my_list.append(2)
    my_list.append(20)
    my_list.append(3)
    my_list.prepand(100)
    my_list.insert_after_node(my_list.head.next, 120)
    my_list.insert_after_node(None, 120)
    print(my_list.traverse())
    print(my_list.count_nodes())
    print(my_list.middle_element())
