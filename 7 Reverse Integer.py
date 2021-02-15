class Solution:
    def reverse(self, x: int) -> int:
        maxx = pow(2,31) - 1
        minn = -pow(2,31)
        if x < 0 :
            y = -x
        else:
            y = x
        s = str(y)
        s = s[::-1]
        res = int(s)
        res = res if x >= 0 else -res
        if res >= maxx or res <= minn:
            return 0
        else:
            return res
            