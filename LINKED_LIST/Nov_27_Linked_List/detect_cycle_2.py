# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        visited = {}
        temp = head
        while temp:
            if temp in visited.keys():
                return temp
            else:
                visited[temp]=1
                temp = temp.next    
        return None 