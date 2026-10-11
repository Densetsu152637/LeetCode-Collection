# 1768. Merge Strings Alternately
def mergeAlternately(self, word1: str, word2: str) -> str:
    return_string: str = ""
    i: int = 0
    iterations = max(len(word1), len(word2))
    while i < iterations:
        
        if (i < len(word1)):
            return_string += word1[i]
        if (i < len(word2)):
            return_string += word2[i]
            
        i += 1
            
    return return_string