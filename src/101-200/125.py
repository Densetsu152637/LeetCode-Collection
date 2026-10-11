# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:        
        n = len(s)
        if n < 2:
            return True
        
        l = 0
        r = len(s) - 1        
        while l < n and not s[l].isalnum():
            l += 1            
        while r > 0 and not s[r].isalnum():
            r -= 1
        
        while l < r:
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1            
            while l < n and not s[l].isalnum():
                l += 1            
            while r > 0 and not s[r].isalnum():
                r -= 1         
            
        return True  
    
    
if __name__ == "__main__":
    s = ".,"
    print(Solution.isPalindrome(None, s))
        
        