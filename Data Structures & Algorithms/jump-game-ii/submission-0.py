class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthestReachable = 0
        currentEnd = 0

        for i in range(len(nums) - 1):
            farthestReachable = max(farthestReachable, i + nums[i])

            if i == currentEnd:
                jumps += 1
                currentEnd = farthestReachable

        return jumps