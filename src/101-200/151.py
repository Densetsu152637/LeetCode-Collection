# 151. Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        
        cleaned = " ".join(s.split())        
        space_indexes = [i for i, char in enumerate(cleaned) if char == ' ']
        ret = []
        p = 0
        
        for space in space_indexes:
            ret.append(cleaned[p:space])
            print(cleaned[p:space])
            p = space + 1     
        
        ret.append(cleaned[p:])            
        ret.reverse()           
        return " ".join(ret)
        
        
        
if __name__ == "__main__":
    s = "the sky is blue"
    print(Solution.reverseWords(None, s))
        
        