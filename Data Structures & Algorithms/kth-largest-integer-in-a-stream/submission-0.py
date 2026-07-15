from heapq import heapify, heappush, nsmallest

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-n for n in nums]
        heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heappush(self.heap, -val)
        return -nsmallest(self.k, self.heap)[-1]