#########################区间DP模板#########################

maxn = 110
inf  = 1000000000
init = 1
dp = [[0] * (maxn) for _ in range(maxn)]
a = [''] * maxn

# min、max、sum
def IntervalDP_Opt(a, b):
    return min(a, b)

# 计算区间 [l, r] 的值
def IntervalDP_CalcState(l, r):
    ans = inf
    for k in range(l, r):
        ans = IntervalDP_Opt(ans, dp[l][k] + dp[k+1][r])
    if a[l] == a[r]:
        ans = IntervalDP_Opt(ans, dp[l+1][r])
        ans = IntervalDP_Opt(ans, dp[l][r-1])
    return ans

# 固定模板，一般情况不需要修改
def IntervalDP_Solve(maxlen, maxr):
    ans = inf
    # 1、枚举区间长度
    for i in range(1, maxlen + 1):
        # 2、枚举区间起点
        for j in range(1, maxr - i + 2):
            l = j
            r = j + i - 1
            if i == 1:
                dp[l][r] = init
            else:
                dp[l][r] = IntervalDP_CalcState(l, r)
            if i == maxlen:
                ans = IntervalDP_Opt(ans, dp[l][r])
    return ans

#########################区间DP模板#########################

# 主逻辑
s = input().strip()
n = len(s)
# 将字符串存储到a数组，索引从1开始
for i in range(1, n + 1):
    a[i] = s[i-1]

result = IntervalDP_Solve(n, n)
print(result)
