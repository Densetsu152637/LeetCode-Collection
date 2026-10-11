# 62. Unique Paths

from functools import cache

@cache
def factorial(n: int):
    if n < 1:
        return 1
    return n * factorial(n - 1)

class Solution:
    
    def uniquePaths(self, m: int, n: int) -> int:        
        top = factorial(m + n - 2)
        bottom = factorial(m - 1) * factorial(n - 1)        
        return top // bottom