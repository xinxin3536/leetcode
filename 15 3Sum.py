class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dict2 = {}
        result = []
        for i in range(0,len(nums)):
            dict2[nums[i]] = i
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                tmp = -(nums[i] + nums[j])
                if tmp in dict2:
                    if dict2[tmp] != i and dict2[tmp] != j and dict2[tmp] > j:
                        res = [nums[i],nums[j],tmp]
                        result.append(res)
        endResult = []
        for i in result:
            i.sort()
        for i in result:
            if i not in endResult:
                endResult.append(i)
        return endResult
            
        