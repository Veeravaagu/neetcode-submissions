# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            res.append(q[-1].val)
            for i in range(len(q)):
                root = q.popleft()
                if root:
                    if root.left:
                        q.append(root.left)
                    if root.right:
                        q.append(root.right)
        return res

        