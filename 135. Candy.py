class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1] * len(ratings)

        for i in range(0,len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                res[i+1] = res[i]+1
        #end不为-1是因为第一个元素不需要与最后一个元素比较r[-1]>r[0]
        for i in range(len(ratings)-1,0,-1):
            if ratings[i-1] > ratings[i]:
                res[i-1] = max(res[i-1],res[i]+1)
        return sum(res)




