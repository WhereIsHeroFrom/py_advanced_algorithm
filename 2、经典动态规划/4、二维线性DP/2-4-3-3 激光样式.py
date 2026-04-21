# dp[i][0] 代表第i个激光器关闭的方案数
# dp[i][1] 代表第i个激光器打开的方案数

n = 30
dp = [[0]*2 for _ in range(n+1)]
dp[1][0] = 1
dp[1][1] = 1

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]

print(dp[30][0] + dp[30][1])
