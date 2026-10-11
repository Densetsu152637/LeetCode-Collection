# 1657. Determine if Two Strings Are Close
def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
        
    freq1: list[int] = [0] * 26
    freq2: list[int] = [0] * 26

    for i in range(len(word1)):
        freq1[ord(word1[i]) - ord("a")] += 1
        freq2[ord(word2[i]) - ord("a")] += 1
        
    for i in range(len(freq1)):
        if freq1[i] == 0 and freq2[i] > 0:
            return False
        if freq2[i] == 0 and freq1[i] > 0:
            return False

    freq1.sort()
    freq2.sort()
            
    return freq1 == freq2