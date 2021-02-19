class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        res = []
        tmp,tmp_Sum = 0, sum(nums)
        for i in nums:
            tmp += i
            res.append(i)
            if tmp > tmp_Sum - tmp:
                break
        return res