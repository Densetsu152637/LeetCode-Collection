# 1456. Maximum Number of Vowels in a Substring of Given Length
def maxVowels(s: str, k: int) -> int:
    if len(s) < k:
        return 0
    
    vowel_list = [0]*len(s)
    for (i, char) in enumerate(s):
        if char in {"a", "e", "i", "o", "u"}:
            vowel_list[i] = 1            
            
    if len(s) == k:
        return sum(vowel_list)
    
    vowels = [0]*(len(vowel_list) - k + 1)
    vowels[0] = sum(vowel_list[0:k])
    
    for i in range(1, len(s) - k + 1):
        vowels[i] = vowels[i-1] - vowel_list[i-1] + vowel_list[i+k-1]
                        
    return max(vowels)