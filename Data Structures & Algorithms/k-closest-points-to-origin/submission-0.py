from _heapq import heappop
import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heap = []

        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)

            heapq.heappush(heap, (-distance, point))

            if len(heap) > k:
                heapq.heappop(heap)

        for pair in heap:
            result.append(pair[1])
    
        return result


    