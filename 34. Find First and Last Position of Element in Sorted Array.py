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

#二分法
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        if len(nums) == 0:
            return res
        l , r = 0, len(nums)-1
        while l<=r:
            mid = l + ((r - l) >> 1)
            if nums[mid] >= target:
                r = mid - 1
            else :
                l = mid + 1
        if l != len(nums) and nums[l] == target:
            res[0] = l
        else:
            return res
        
        l , r = 0, len(nums)-1
        while l<=r:
            mid = l + ((r - l) >> 1)
            if nums[mid]  <= target:
                l = mid + 1
            else :
                r = mid - 1
        res[1] = r
        return res

#网上 bisect方法
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect(nums, target)
        if left != len(nums) and nums[left] == target:
            return [left, right-1]
        else:
            return [-1,-1]