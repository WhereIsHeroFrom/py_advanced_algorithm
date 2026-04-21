### 数据输入
n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
### 初始化
dp = [[-10**9]*(k+1) for _ in range(n+1)]
dp[0][0] = 0

### 状态转移
for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][0], 0) + a[i]
    for j in range(1, k+1):
        # 当前这个元素 -     不删除           删除
        dp[i][j] = max(dp[i-1][j] + a[i], dp[i-1][j-1])

### 计算结果
ans = -10**9
for i in range(1, n+1):
    for j in range(0, k+1):
        ans = max(ans, dp[i][j])

### 输出结果
print(ans)
