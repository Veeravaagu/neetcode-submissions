# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Was not able to grasp the problem statement but calrified with vasanth and misunderstood that I need compare with root but not the max for when visited so even if misunderstood I could solve it but was stuck in adding the count but was able recognise it was similar to fibonacci recursion.
        if not root:
            return 0
        return self.findGoodNodes(root, root.val)
    def findGoodNodes(self, root: TreeNode, node: int) -> int:
        if not root:
            return 0
        if root.val >= node:
            count = 1
        else:
            count = 0
        node = root.val if root.val > node else node
        return count + self.findGoodNodes(root.left, node) + self.findGoodNodes(root.right, node)
        