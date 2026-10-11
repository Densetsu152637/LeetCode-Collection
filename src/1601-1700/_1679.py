# 1679. Max Number of K-Sum Pairs TODO
def maxOperations(nums: list[int], k: int) -> int:
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        pass