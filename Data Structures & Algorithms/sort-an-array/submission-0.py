class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr1, arr2):
            s1 = s2 = 0
            f1, f2 = len(arr1), len(arr2)

            ans = []
            while s1 < f1 and s2 < f2:
                if arr1[s1] > arr2[s2]:
                    ans.append(arr2[s2])
                    s2 += 1
                else:
                    ans.append(arr1[s1])
                    s1 += 1
                
            ans.extend(arr1[s1:])
            ans.extend(arr2[s2:])
            return ans
        
        print(merge([1,3,4,4,6], [1,2,2,4,5]))

        def mergeSort(arr):
            n = len(arr)
            if n <= 1:
                return arr
            
            return merge(mergeSort(arr[:n//2]),  mergeSort(arr[n//2:]))
        
        return mergeSort(nums)
            