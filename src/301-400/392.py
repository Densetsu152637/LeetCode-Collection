# 392. Is Subsequence
def isSubsequence(s: str, t: str) -> bool:
    
    if (len(s) == 0):
        return True
    
    seq_arr = [False]*len(s)
    seq_p: int = 0
        
    for c in t:
        if c == s[seq_p]:
            seq_arr[seq_p] = True
            seq_p += 1
            if (seq_arr[-1] == True):
                return True
            
    return seq_arr[-1] == True