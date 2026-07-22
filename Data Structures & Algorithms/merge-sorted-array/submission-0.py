class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n1 = m - 1
        n2 = n - 1
        p = len(nums1) - 1
        while 0 <= n1 and 0 <= n2:
            if nums1[n1] > nums2[n2]:
                nums1[p] = nums1[n1]
                n1 -= 1
            else:
                nums1[p] = nums2[n2]
                n2 -= 1
            
            p -= 1

        while 0 <= n2:
            nums1[p] = nums2[n2]
            n2 -= 1
            p -= 1
        


        