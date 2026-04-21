mod = 1000000007
n = int(input())
s = []
for i in range(n):
    row = input().strip()
    s.append(row)

dp = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if s[i][j] == '*':
            dp[i][j] = 0
        else:
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:   # 从左边过来
                dp[i][j] = dp[i][j-1]
            elif j == 0:   # 从上边过来
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % mod

print(dp[n-1][n-1])
