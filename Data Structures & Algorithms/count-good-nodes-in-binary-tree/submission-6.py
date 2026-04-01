# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root, maxValue):
            if not root:
                return
            if root.val >= maxValue:
                self.count += 1
                maxValue = max(maxValue, root.val)
            dfs(root.left, maxValue)
            dfs(root.right, maxValue)
            return
        dfs(root, root.val)
        return self.count
                
            
            

        