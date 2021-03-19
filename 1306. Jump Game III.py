class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        isPass = [0] * len(arr)

        def dfs(n:int):
            if isPass[n] == 1:
                return False
            if isPass[n] == 0 and arr[n] == 0:
                return True
            left,right = False,False
            isPass[n] = 1
            if 0 <=  n-arr[n] and n-arr[n] < len(arr):
                left = dfs(n-arr[n])
            if 0 <=  n+arr[n] and n+arr[n] < len(arr):
                right = dfs(n+arr[n])
            return right or left
        return dfs(start)