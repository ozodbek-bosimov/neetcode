class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def counting_sort():
            minVal, maxVal = min(nums), max(nums)
            count = [0]*(maxVal - minVal + 1)

            for num in nums:
                count[num - minVal] += 1

            index = 0
            for val in range(minVal, maxVal + 1):
                while count[val - minVal] > 0:
                    nums[index] = val
                    index += 1
                    count[val - minVal] -= 1

        counting_sort()
        return nums

# K = maxVal − minVal + 1
# N = nums.length
# Time : O(N + K)
# Space: O(K)