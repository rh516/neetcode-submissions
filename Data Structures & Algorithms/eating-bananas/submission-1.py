import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        answer = 0
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            totalTime = 0
            for pileSize in piles:
                totalTime += math.ceil(pileSize / mid)

            if totalTime <= h:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer
        