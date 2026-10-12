class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        
        it = nums[0]
        count = 1        
        
        for i in range(1, len(nums)):
            # if it is it then increase count
            if nums[i] == it:
                count += 1
                
            else:
                count -= 1     
                # if count is 0 then swap the target   
                if count <= 0:
                    it = nums[i]
                    count = 1
                    
        return it