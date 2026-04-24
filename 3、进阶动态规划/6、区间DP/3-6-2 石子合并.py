#########################区间DP模板#########################

maxn = 210
inf  = 1000000000
init = 0
dp = [[0] * (maxn) for _ in range(maxn)]
sum_ = []

# min、max、sum
def IntervalDP_Opt(a, b):
    return min(a, b)

# 计算区间 [l, r] 的值
def IntervalDP_CalcState(l, r):
    ans = inf
    for k in range(l, r):
        v = dp[l][k] + dp[k+1][r] + (sum_[r] - sum_[l-1])
        ans = IntervalDP_Opt(ans, v)
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
n = int(input())
sum_ = [0] * (n + 1)
a = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    sum_[i] = sum_[i-1] + a[i]

result = IntervalDP_Solve(n, n)
print(result)
