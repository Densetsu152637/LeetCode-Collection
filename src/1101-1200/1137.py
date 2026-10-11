# 1137. N-th Tribonacci Number

class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        t_0 = 0
        t_1 = 1
        t_2 = 1
        t_3 = 2
        
        for i in range(2, n):
            t_3 = t_2 + t_1 + t_0
            t_0, t_1, t_2 = t_1, t_2, t_3
        
        return t_3
        
            
        