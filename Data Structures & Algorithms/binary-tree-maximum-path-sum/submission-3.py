# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maximum = root.val
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            cur_sum = root.val + max(0, left) + max(0, right)
            self.maximum = max(self.maximum, cur_sum)
            return root.val + max(max(0, left), max(0, right))
        dfs(root)
        return self.maximum
            