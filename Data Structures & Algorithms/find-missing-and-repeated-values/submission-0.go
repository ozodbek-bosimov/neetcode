// T: O(n^2) 
// S: O(1)
func findMissingAndRepeatedValues(grid [][]int) []int {
    n := len(grid)
    N := n * n
    expected_sum := N * (N + 1) / 2
    expected_sq_sum := N * (N + 1) * (2*N + 1) / 6
    real_sum := 0
    real_sq_sum := 0
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            val := grid[i][j]
            real_sum += val
            real_sq_sum += val*val
        }
    }
    diff := expected_sum - real_sum // n - d
    kv_diff := expected_sq_sum - real_sq_sum // n*n - d*d = (n - d)*(n + d)
    b := kv_diff/diff // n + d
    need := (diff + b)/2 
    duplicate := b - need
    return []int{duplicate, need}
    
}





