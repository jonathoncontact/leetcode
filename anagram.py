def isAnagram(s,t):
    if len(s) != len(t):
        return False
    
    #these are dictionaries as we will be counting a key
    #and value. the char and the amount of times it appears
    countS,countT = {},{}
    #established both strings are the same length 
    # so only need to use one of the range(len(s)) 
    # for this example.
    for i in range(len(s)):
        #use the .get to avoid key error
        #basically returns a 0 then + 1 
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True
s = "xac"
t = "tac"
result = isAnagram(s, t)
print(result)