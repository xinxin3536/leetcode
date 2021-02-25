class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1,rowIndex+1):
            tmp = [1]
            for j in range(1,i):
                tmp.append( res[j]+res[j-1])
            tmp.append(1)
            res = tmp
        return res