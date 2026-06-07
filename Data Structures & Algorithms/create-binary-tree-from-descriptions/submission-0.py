# https://leetcode.com/problems/create-binary-tree-from-descriptions/

# T: O(n)
# S: O(n)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()
        for description in descriptions:
            parent, child, isLeft = description

            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            children.add(child)
            
            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

        for key, node in nodes.items():
            if key not in children:
                return node



# Example:
# Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
# Output: [50,20,80,15,17,19]
solution = Solution()
root = solution.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
print(f"             {root.val}   ")
print(f"           /    \\")
print(f"          {root.left.val}    {root.right.val}")
print(f"         /  \\   /")
print(f"        {root.left.left.val}  {root.left.right.val} {root.right.left.val}")

#      50   
#    /    \
#   20     80
#  /  \   /
# 15  17 19



