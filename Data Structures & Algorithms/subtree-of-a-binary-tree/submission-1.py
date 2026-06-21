# n and m are the number of nodes in root and subRoot
# T: O(m * n)
# S: O(n + m)
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(currRoot, subRoot):
            if currRoot is None and subRoot is None:
                return True
            if currRoot is None or subRoot is None:
                return False
            if currRoot.val != subRoot.val:
                return False
            
            return isSame(currRoot.left, subRoot.left) and isSame(currRoot.right, subRoot.right)
        
        def dfs(node):
            if node is None:
                return False
            if isSame(node, subRoot):
                raise StopIteration
            return dfs(node.left) or dfs(node.right)
        
        try:
            dfs(root)
            return False
        except StopIteration:
            return True