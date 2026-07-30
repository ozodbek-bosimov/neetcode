class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                l, r = j + 1, n - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l - 1] == nums[l]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif s > target:
                        r -= 1
                    else:
                        l += 1
        
        return ans