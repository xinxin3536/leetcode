class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0 
        if len(s)==0:
            return True
        if len(t) == 0:
            return False
        for i in range(0,len(t)):
            if t[i] == s[j]:
                j += 1
            if j >= len(s):
                break
        if j == len(s):
            return True
        else:
            return False