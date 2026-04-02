# Time complexity: O(n)
# Space complexity O(h)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node is None:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            if abs(l - r) > 1:
                raise ValueError

            return max(l, r) + 1
        
        try:
            dfs(root)
            return True
        except ValueError:
            return False
