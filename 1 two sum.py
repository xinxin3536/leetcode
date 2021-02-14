class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(0,len(nums)):
            dict1[nums[i]] = i
        for j in range(0,len(nums)):
            tmp = target - nums[j]
            if tmp in dict1  and j != dict1[tmp]:
                return [j,dict1[tmp]]