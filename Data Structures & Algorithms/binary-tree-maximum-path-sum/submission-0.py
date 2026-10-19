# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -1000000

        def dfs(node):
            nonlocal maxSum

            if not node:
                return 0

            leftGain = max(0, dfs(node.left))
            rightGain = max(0, dfs(node.right))
            sumThroughNode = leftGain + node.val + rightGain

            maxSum = max(maxSum, sumThroughNode)

            return node.val + max(leftGain, rightGain)

        dfs(root)

        return maxSum