# 2215. Find the Difference of Two Arrays
def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set1 = set(nums1)
    set2 = set(nums2)
    both_set = set(nums1 + nums2)
        
    return [list(both_set - set2), list(both_set - set1)]