# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Time Complexity: O(n) — each node is visited exactly once
# Space Complexity: O(h) — due to the recursion stack (where h is the height of the tree)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if node is None:
                return 0
            
            lh = dfs(node.left)
            rh = dfs(node.right)

            if lh + rh > self.ans:
                self.ans = lh + rh
            
            return max(lh, rh) + 1
        
        dfs(root)
        return self.ans

