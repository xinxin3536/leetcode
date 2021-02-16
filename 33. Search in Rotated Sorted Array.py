class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0 ,len(nums)-1
        while l <= r:
            mid = l + ((r-l) >> 1)
            if nums[mid] == target:
                return mid
            #落在同一数组的情况，同时落在数组1 或 数组2
            elif nums[mid] >= nums[l]:
                #target 落在 left 和 mid 之间，则移动我们的right，完全有序的一个区间内查找
                if nums[mid] > target and nums[l] <= target:
                    r = mid - 1
                #target 落在right和 mid 之间，有可能在数组1， 也有可能在数组2
                elif nums[mid] < target or nums[l] > target:
                    l = mid + 1
            #不落在同一数组的情况，left 在数组1， mid 落在 数组2
            elif nums[mid] < nums[l]:
                #有序的一段区间，target 在 mid 和 right 之间
                if nums[mid] < target and nums[r] >= target:
                    l = mid + 1
                #两种情况，target 在left 和 mid 之间
                elif nums[mid] > target or nums[r] < target:
                    r = mid - 1
        #not found
        return -1 