# 1732. Find the Highest Altitude
def largestAltitude(gain: list[int]) -> int:
    
    net_alt = [0]*len(gain)
    net_alt[0] = gain[0]
    
    for i in range(1, len(gain)):
        net_alt[i] = net_alt[i-1] + gain[i]
        
    print(net_alt)
        
    return max(max(net_alt), 0)