class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)
        if not head:
            new_node = Node(data)
            new_node.next = new_node
            return new_node
        if new_node.data < head.data:
            curr = head
            while curr.next != head:
                curr = curr.next
            curr.next = new_node
            new_node.next = head
            return new_node
        else:
            curr = head
            while curr.next != head:
                if curr.next.data > new_node.data:
                    break
                curr = curr.next
            temp = curr.next
            curr.next = new_node
            new_node.next = temp
            return head