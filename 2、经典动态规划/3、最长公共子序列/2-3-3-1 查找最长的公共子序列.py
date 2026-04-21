def getLCS(n, a, m, b, dp, path):
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i] == b[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                path[i][j] = 0
            elif dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = 0
                path[i][j] = 1
            else:
                dp[i][j] = 0
                path[i][j] = 2
    return dp[n][m]

def constructLCS(x, a, y, b, path, ans):
    i, j = x, y
    ansSize = 0
    while i > 0 and j > 0:
        if path[i][j] == 0:
            ans.append(a[i])
            ansSize += 1
            i -= 1
            j -= 1
        elif path[i][j] == 1:
            i -= 1
        elif path[i][j] == 2:
            j -= 1
    ans.reverse()

a = input().strip()
b = input().strip()

n = len(a)
m = len(b)

# 调整数组索引，使其从1开始
a = [''] + list(a)
b = [''] + list(b)

maxn = 1010
maxm = 1010
dp = [[0]*(maxm) for _ in range(maxn)]
path = [[0]*(maxm) for _ in range(maxn)]

getLCS(n, a, m, b, dp, path)

x, y = 1, 1
for i in range(1, n+1):
    for j in range(1, m+1):
        if dp[i][j] > dp[x][y]:
            x = i
            y = j

ans = []
constructLCS(x, a, y, b, path, ans)

print(''.join(ans))
