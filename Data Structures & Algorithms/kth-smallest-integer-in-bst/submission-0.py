# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Didn't understand the question had use GPT but it got easier once i did had the correct idea to stop when len of k is reached but was wrong
        self.k = k
        self.res = None
        def inorder(root: Optional[TreeNode]):
            if not root or self.res is not None:
                return
            inorder(root.left)
            self.k -= 1
            if not self.k:
                self.res = root.val
            inorder(root.right)
        inorder(root)
        return self.res
        