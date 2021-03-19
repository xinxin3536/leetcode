class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        s = str(x)
        s = s[::-1]
        if str(x) == s:
            return True
        else:
            return False