class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        temp = [0]*len(nums)

        def merge(l, m, r):
            i, j = l, m + 1
            p = 0
            while i <= m and j <= r:
                if nums[i] <= nums[j]:
                    temp[p] = nums[i]
                    i += 1
                else:
                    temp[p] = nums[j]
                    j += 1
                p += 1
            while i <= m:
                temp[p] = nums[i]
                i += 1
                p += 1
            while j <= r:
                temp[p] = nums[j]
                j += 1
                p += 1
            nums[l: r+1] = temp[: p]


        def merge_sort(l, r):
            if l < r:
                m = (l + r) // 2
                merge_sort(l, m)
                merge_sort(m + 1, r)
                merge(l, m, r)


        merge_sort(0, len(nums) - 1)
        return nums