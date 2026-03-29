class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            # update diameter at this node
            self.diameter = max(self.diameter, left + right)

            # return height to parent
            return 1 + max(left, right)

        height(root)
        return self.diameter