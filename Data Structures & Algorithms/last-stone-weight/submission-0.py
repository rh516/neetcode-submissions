import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
            create max heap

            while len(heap) > 1:
                remove top 2
                take the diff of weights, if > 0:
                    add diff of weights to heap
                
            return heap[0] if 1 stone left, ohterwise return 0


        '''

        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)

        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)

            diff = abs(stone1 - stone2)

            if diff > 0:
                heapq.heappush(heap, -diff)

        return -heap[0] if len(heap) > 0 else 0

        