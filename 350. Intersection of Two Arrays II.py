class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = collections.Counter()
        for i in range(0,len(nums1)):
            dict1[nums1[i]] += 1
        res = []
        for i in range(0,len(nums2)):
            if nums2[i] in dict1 and dict1[nums2[i]] > 0:
                dict1[nums2[i]] -= 1
                res.append(nums2[i])
        return res