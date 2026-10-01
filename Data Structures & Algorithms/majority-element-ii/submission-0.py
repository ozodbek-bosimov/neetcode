class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        can1 = 0.4
        can2 = 0.4
        c1 = 0
        c2 = 0

        for num in nums:
            if num == can1:
                c1 += 1
            elif num == can2:
                c2 += 1
            elif c1 == 0:
                can1 = num
                c1 = 1
            elif c2 == 0:
                can2 = num
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        count1 = 0
        count2 = 0
        for num in nums:
            if num == can1:
                count1 += 1
            elif num == can2:
                count2 += 1
        lim = len(nums) //3
        ans = []
        if count1 > lim:
            ans.append(can1)
        if count2 > lim:
            ans.append(can2)

        return ans
