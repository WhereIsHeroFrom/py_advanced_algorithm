#########################区间DP模板#########################

maxn = 410
inf  = 0
init = 0
dp = [[0] * (maxn) for _ in range(maxn)]
a = [0] * maxn
mul = [[0 for _ in range(maxn)] for _ in range(maxn)]

# min、max、sum
def IntervalDP_Opt(a, b):
    return max(a, b)

# 计算区间 [l, r] 的值
def IntervalDP_CalcState(l, r):
    ans = inf
    for k in range(l, r):
        # dp[l][k] ... dp[k+1][r]
        a_val = mul[l][k]
        b_val = mul[k+1][r]
        v = dp[l][k] + dp[k+1][r] + (a_val * b_val) // 10
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
n2 = n * 2
a = [0] + list(map(int, input().split())) * 2
for i in range(1, n + 1):
    a[n + i] = a[i]

# 预处理mul数组
for i in range(1, n2 + 1):
    mul[i][i-1] = 1
    for j in range(i, n2 + 1):
        mul[i][j] = (mul[i][j-1] * a[j]) % 10

result = IntervalDP_Solve(n, n2)
print(result)