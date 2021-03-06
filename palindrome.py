class Solution(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dp = [[0 for _ in range(len(arr)+1)] for _ in range(len(arr)+1)]
        for l in range(1, len(arr)+1):
            for i in range(len(arr)-l+1):
                j = i+l-1
                if l == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1+dp[i+1][j]
                    if arr[i] == arr[i+1]:
                        dp[i][j] = min(dp[i][j], 1+dp[i+2][j])
                    for k in range(i+2, j+1):
                        if arr[i] == arr[k]:
                            dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k+1][j])
        return dp[0][len(arr)-1]
val=Solution()
m=int(input())
rows=list(map(int,input().split()))
print(val.minimumMoves(rows))
