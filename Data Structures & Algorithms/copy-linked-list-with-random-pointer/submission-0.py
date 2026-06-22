"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {None : None}
        dummy = Node(0)
        new_curr = dummy
        curr = head
        
        while curr:
            new_node = Node(curr.val)
            node_map[curr] = new_node 
            new_curr.next = new_node
            new_curr = new_curr.next
            curr = curr.next

        new_curr = dummy.next
        curr = head
        
        while curr:
            new_curr.random = node_map[curr.random]  
            new_curr = new_curr.next
            curr = curr.next

        return dummy.next