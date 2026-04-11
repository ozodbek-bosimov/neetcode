/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

// Time Complexity: O(n) — each node is visited exactly once
// Space Complexity: O(h) — due to the recursion stack (where h is the height of the tree)

func diameterOfBinaryTree(root *TreeNode) int {
    maxd := 0
    dfs(root, &maxd)
    return maxd
}

func dfs(node *TreeNode, maxd *int) int {
    if node == nil {
        return 0
    }

    lh := dfs(node.Left, maxd)
    rh := dfs(node.Right, maxd)

    sum := lh + rh
    if sum > *maxd {
        *maxd = sum
    }

    if lh > rh {
        return lh + 1
    }
    return rh + 1
}