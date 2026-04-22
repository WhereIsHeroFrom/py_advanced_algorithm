###################LCS模板###################
def getLCS(n, a, m, b, dp, path):
    # dp[i][j] 代表 a[1:i] 和 b[1:j] 
    # 这两个数组的最长公共子序列的长度
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i] == b[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                path[i][j] = 0
            elif dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                path[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1]
                path[i][j] = 2
    return dp[n][m]
###################LCS模板###################


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

### 数据输入
a = input()
b = input()
n, m = len(a), len(b)

### 数据处理
a = [''] + list(a)
b = [''] + list(b)
dp = [[0]*(m + 1) for _ in range(n + 1)]
path = [[0]*(m + 1) for _ in range(n + 1)]

### 算法过程
getLCS(n, a, m, b, dp, path)

### 数据处理
x, y = 1, 1
for i in range(1, n+1):
    for j in range(1, m+1):
        if dp[i][j] > dp[x][y]:
            x = i
            y = j

ans = []
constructLCS(x, a, y, b, path, ans)
print(''.join(ans))
