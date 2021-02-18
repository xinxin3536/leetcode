class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        j = 0
        for i in range(0,len(s)):
            if s[i] >= g[j]:
                cnt += 1
                j += 1
            if j >= len(g):
                break
            
        return cnt