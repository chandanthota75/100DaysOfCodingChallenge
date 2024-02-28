class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Solution:
    def mergeResult(self, h1, h2):
        dummy = Node(0)
        current = dummy
        while h1 is not None or h2 is not None:
            if h1 is None:
                current.next = h2
                break
            elif h2 is None:
                current.next = h1
                break
            if h1.data <= h2.data:
                current.next = h1
                h1 = h1.next
            else:
                current.next = h2
                h2 = h2.next
            current = current.next
        prev = None
        current = dummy.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev