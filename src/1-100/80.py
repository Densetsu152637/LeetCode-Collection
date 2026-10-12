# 26. Remove Duplicates from Sorted Array

from collections import Counter

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        
        counts = Counter(nums)
        
        for i in range(n - 1, -1, -1):
            t = nums[i]
            # is the same
            if counts[t] > 2:
                nums.pop(i)
                counts[t] -= 1
            
        return len(nums)
        