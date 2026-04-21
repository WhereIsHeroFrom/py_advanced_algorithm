#############最大子数组和模板#############
# a列表的第0个元素是不用的，从第1个元素开始
def getMSS(n, a, dp):
    # dp[i] 代表以第 i 个数结尾的最大子段和
    dp[0] = 0
    for i in range(1, n+1):
        dp[i] = a[i] + max(dp[i-1], 0)
    # 转换成前 i 个元素的最大子段和
    dp[0] = -10**18
    for i in range(1, n+1):
        dp[i] = max(dp[i], dp[i-1])
    return dp[n]
#############最大子数组和模板#############

def swap(n, a):
    a[1:n+1] = a[1:n+1][::-1]

### 数据输入
n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))
dppre = [0] * (n+1)
dppost = [0] * (n+1)

### 预处理
getMSS(n, a, dppre)
swap(n, a)
getMSS(n, a, dppost)
swap(n, dppost)

### 计算结果
ans = -10**18
for i in range(1, n - k):
    if i + k + 1 <= n:
        ans = max(ans, dppre[i] + dppost[i + k + 1])

print(ans)
