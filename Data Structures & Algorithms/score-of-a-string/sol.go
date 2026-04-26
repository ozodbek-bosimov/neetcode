// https://leetcode.com/problems/score-of-a-string/
package main

import "fmt"

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
// Time: O(n)  — iterate through string once
// Space: O(1) — constant extra space
func scoreOfString(s string) int {
    res := 0
    prev_val := int(s[0])

    for _, ch := range s[1:] {
        curr_val := int(ch)
        res += abs(curr_val - prev_val)
        prev_val = curr_val 
    }

    return res
}




func main() {
	fmt.Println(scoreOfString("zaz")) // 50
}