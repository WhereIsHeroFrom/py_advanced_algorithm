n = int(input())
mat = []
for i in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

dp = [[0]*n for _ in range(n)]
dp[0][0] = mat[0][0]

for i in range(1, n):
    dp[i][i] = mat[i][i] + dp[i-1][i-1]
    dp[i][0] = mat[i][0] + dp[i-1][0]
    for j in range(1, i):
        dp[i][j] = mat[i][j] + max(dp[i-1][j-1], dp[i-1][j])

if n % 2 == 1:
    ans = dp[n-1][n//2]
else:
    ans = max(dp[n-1][n//2-1], dp[n-1][n//2])

print(ans)
