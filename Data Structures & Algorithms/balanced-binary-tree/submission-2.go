/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// Time complexity: O(n)
// Space complexity O(h)
func isBalanced(root *TreeNode) bool {
    return dfs(root) != -1
}

func dfs(node *TreeNode) int {
    if node == nil {
        return 0
    }

    l := dfs(node.Left)
    if l == -1 { return -1 }

    r := dfs(node.Right)
    if r == -1 { return -1 }

    diff := l - r
    if diff > 1 || diff < -1 {
        return -1
    }

    if l > r {
        return l + 1
    }
    return r + 1
}