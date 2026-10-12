# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        last = None
        
        for i in range(n - 1, -1, -1):
            curr = nums[i]
            # is the same
            if curr == last:
                nums.pop(i)
                
            last = curr
            
        return len(nums)
        