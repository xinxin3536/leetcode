class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        l,r = 0,len(nums)-1
        while l <= r:
            mid = l + ((r-l)>>1)
            if nums[mid] >= target:
                r = mid - 1
            else :
                l = mid + 1
        return l