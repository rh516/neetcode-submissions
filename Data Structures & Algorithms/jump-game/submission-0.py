class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthestReachable = 0

        for i in range(len(nums)):
            if i > farthestReachable:
                return False

            farthestReachable = max(
                farthestReachable,
                i + nums[i]
            )

        return True