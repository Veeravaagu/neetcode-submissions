class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = None

        def dfs(node):
            if not node or self.res is not None:
                return
            
            dfs(node.left)

            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return

            dfs(node.right)

        dfs(root)
        return self.res