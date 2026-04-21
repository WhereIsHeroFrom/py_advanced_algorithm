def getMSS(n, a, dp):
    # dp[i] 表示以第 i 个数结尾的最大子段和
    ans = -10**18
    dp[0] = 0
    for i in range(1, n+1):
        dp[i] = a[i] + max(dp[i-1], 0)
        ans = max(ans, dp[i])
    return ans

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
print(getMSS(n, a, dp))
