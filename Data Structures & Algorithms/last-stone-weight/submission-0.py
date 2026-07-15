from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapify(heap)

        while len(heap) > 1:
            x, y = -heappop(heap), -heappop(heap)

            if x == y:
                continue

            if x < y:
                heappush(heap, -(y - x))
            elif x > y:
                heappush(heap, -(x - y))

        return -heap[0] if heap else 0