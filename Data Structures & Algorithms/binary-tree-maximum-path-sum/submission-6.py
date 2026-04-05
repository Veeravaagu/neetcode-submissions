# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val
        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            nodeMax = root.val + max(0, leftMax) + max(0, rightMax)
            self.maxSum = max(self.maxSum, nodeMax)
            return root.val + max(leftMax, rightMax, 0)
        dfs(root)
        return self.maxSum
            