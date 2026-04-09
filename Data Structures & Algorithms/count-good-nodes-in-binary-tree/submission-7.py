# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal = root.val
        self.count = 0
        def dfs(root, maxVal):
            if not root:
                return
            if root.val >= maxVal:
                self.count += 1
                maxVal = root.val
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

            return 
        dfs(root, maxVal)
        return self.count


        