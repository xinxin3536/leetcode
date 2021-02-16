class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = len(nums)
        cnt = 0
        for i in range(0,len(nums)):
            if nums[i] == val:
                nums[i] = 0
                cnt += 1
        nums.sort(reverse = True)
        return len(nums)-cnt