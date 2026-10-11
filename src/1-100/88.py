# 88. Merge Sorted Array
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l_p = m - 1
        r_p = n - 1
        
        for i in range(m + n - 1, -1, -1):
            
            less_than = (l_p > -1 and r_p > -1) and nums1[l_p] < nums2[r_p]
            
            if (not less_than or r_p == -1) and l_p >= 0:
                nums1[i] = nums1[l_p]
                l_p -= 1
                
            elif (less_than or l_p == -1) and r_p >= 0:
                nums1[i] = nums2[r_p]
                r_p -= 1
    
    
if __name__ == "__main__":
    n1 = [1,2,3,0,0,0]
    Solution.merge(None, n1, 3, [2,5,6], 3)    
    print(n1)
    