class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dict1 = {}
        for i in nums:
            if i not in dict1:
                dict1[i]  = 1
            else:
                dict1[i] += 1
        for j in dict1:
            if dict1[j] > 1:
                res = j
                break
        return res