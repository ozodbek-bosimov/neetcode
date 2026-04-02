# Time complexity: O(n)
# Space complexity O(h)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if left==-1 or right==-1:
                return -1

            if abs(right - left) > 1:
                return -1

            return 1 + max(left, right)
        return dfs(root) != -1