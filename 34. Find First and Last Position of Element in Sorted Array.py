class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i,j = -1,-1
        for t in range(0,len(nums)):
            if nums[t] == target:
                i = t
                break
        for t in range(0,len(nums)):
            if nums[t] == target:
                j = t
        return [i,j]