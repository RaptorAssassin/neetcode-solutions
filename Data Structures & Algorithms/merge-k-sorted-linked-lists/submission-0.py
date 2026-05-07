# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [(l.val, i, l) for i, l in enumerate(lists) if l]
        heapq.heapify(heap)

        dummy = ListNode()
        curr = dummy

        while heap:
            smallest = heapq.heappop(heap)
            node = smallest[2]
            curr.next = node
            nxt = node.next
            if nxt: heapq.heappush(heap, (nxt.val, smallest[1], nxt))
            curr = curr.next
     
        return dummy.next