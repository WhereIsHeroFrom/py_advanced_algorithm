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

### 数据输入
n = int(input())
a = [0] + list(map(int, input().split()))
### 初始化
dp = [[0]*(n + 1) for _ in range(n + 1)]
### 预处理
for i in range(1, n+1):
    sub_a = a[i-1:]
    getMSS(len(sub_a)-1, sub_a, dp[i])
### 查询
t = int(input())
while t > 0:
    t -= 1
    l, r = map(int, input().split())
    print(dp[l][r - l + 1])
