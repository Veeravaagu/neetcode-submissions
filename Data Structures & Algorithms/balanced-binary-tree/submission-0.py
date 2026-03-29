# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Had the idea was close but made mistakes took 45 mins so saw solution
        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
# ---- Your original code (as posted) ----
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if root:
#             if not root:
#                 return 0
#             left = self.isBalanced(root.left)
#             right = self.isBalanced(root.right)
#             if abs(left - right) <= 1:
#                 height = 1 + max(left, right)
#                 return height
#             else:
#                 return False
#             return True
#         else:
#             return True
#
# ---- Why this failed ----
# 1) Type contract violation:
#    - isBalanced must return a bool, but this function sometimes returns an int (height).
#      Example: in the "balanced" branch it returns `height` instead of True.
#
# 2) Mixing booleans with heights:
#    - You set `left = self.isBalanced(root.left)` and `right = self.isBalanced(root.right)`,
#      which are booleans, then compute `abs(left - right)` as if they were heights.
#      In Python, True == 1 and False == 0, so this silently produces nonsense for height comparisons.
#
# 3) Contradictory / dead code:
#    - `if root:` immediately followed by `if not root:` inside that block is unreachable.
#      That indicates a broken base case and never executes as intended.
#
# 4) No propagation of "unbalanced" status correctly:
#    - If a subtree is unbalanced, you should bubble that fact up immediately.
#      Here, because left/right are booleans misused as heights, the unbalanced state is not
#      reliably detected or propagated.
#
# 5) Early returns prevent checking both sides properly:
#    - The structure returns inside branches without a clean, consistent evaluation of both subtrees
#      and without maintaining a clear separation between "height computation" and "balanced check".
#
# 6) Missing proper base case for height logic:
#    - For height computations you need `if not node: return 0`.
#      Here, you never compute real heights; you compute booleans and treat them like heights.
#
# ---- Core fix idea (conceptual, not code here) ----
# - Use a helper that returns (balanced: bool, height: int) together, or return height and -1 as a sentinel.
# - Base: None -> (True, 0).
# - Recurse to get (lb, lh) and (rb, rh), then `balanced = lb and rb and abs(lh - rh) <= 1`,
#   and height = 1 + max(lh, rh). Return the boolean to isBalanced.
