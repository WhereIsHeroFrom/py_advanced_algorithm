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

### 输入
n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))
### 数据结构
dp = [[0]*(m + 1) for _ in range(n + 1)]
path = [[0]*(m + 1) for _ in range(n + 1)]
### 输出
print(getLCS(n, a, m, b, dp, path))
