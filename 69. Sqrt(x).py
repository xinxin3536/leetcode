class Solution:
    def mySqrt(self, x: int) -> int:
        l,r,ans = 0,x,-1
        while l<=r:
            mid = l + ((r-l) >> 1)
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            elif mid * mid > x:
                r = mid - 1
        return ans
            