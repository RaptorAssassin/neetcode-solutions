import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        # (distance, point index)

        for i, point in enumerate(points):
            x, y = point
            distance = math.sqrt((0 - x)**2 + (0 - y)**2)
            heapq.heappush(heap, (-distance, i))
            
            if len(heap) > k:
                heapq.heappop(heap)

        closest = [point[1] for point in heap]

        return [points[i] for i in closest]