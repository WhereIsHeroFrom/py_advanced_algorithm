n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

maxn = 100010
maxk = 101
dp = [[-10**9]*(maxk) for _ in range(maxn)]

dp[0][0] = 0
for j in range(1, k+1):
    dp[0][j] = -10**9

for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][0], 0) + a[i]
    for j in range(1, k+1):
        # 当前这个元素 -     不删除           删除
        dp[i][j] = max(dp[i-1][j] + a[i], dp[i-1][j-1])

ans = -10**9
for i in range(1, n+1):
    for j in range(0, k+1):
        ans = max(ans, dp[i][j])

print(ans)
