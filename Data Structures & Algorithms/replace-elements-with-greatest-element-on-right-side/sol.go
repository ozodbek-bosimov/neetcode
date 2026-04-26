// https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
package main

import "fmt"

func replaceElements(arr []int) []int {
	n := len(arr)
	max_right := -1
	for i := n - 1; i >= 0; i-- {
		this_val := arr[i]
		arr[i] = max_right
		if this_val > max_right {
			max_right = this_val
		}
	}
	return arr
}

func main() {
	arr := []int{17, 18, 5, 4, 6, 1}
	result := replaceElements(arr)
	fmt.Println(result)
}
