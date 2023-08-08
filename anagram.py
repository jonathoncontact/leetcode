def isAnagram(s,t):
    if len(s) != len(t):
        return False
    
    countS,countT = {},{}
    for i in range(len(s)):
        #use the .get to avoid key error
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