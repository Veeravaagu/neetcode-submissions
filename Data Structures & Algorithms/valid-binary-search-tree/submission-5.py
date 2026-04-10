# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isBST(low, high, root):
            if not root:
                return True
            if not (low < root.val < high):
                return False
            return isBST(low, root.val, root.left) and isBST(root.val, high, root.right)
        return isBST(float("-inf"), float("inf"), root )
                
        
        