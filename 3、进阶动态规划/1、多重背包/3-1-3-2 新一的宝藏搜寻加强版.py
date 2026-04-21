def opt(a, b):
    if a == -1:
        return b
    if b == -1:
        return a
    return max(a, b)

def Knapsack01(n, V, w, v, dp):
    # 1、初始化
    for i in range(1, V+1):
        dp[i] = -1
    dp[0] = 0
    # 2、状态转移
    for i in range(1, n+1):
        for j in range(V, w[i]-1, -1):
            if dp[j - w[i]] != -1:
                dp[j] = opt(dp[j], dp[j - w[i]] + v[i])

def KnapsackMultiple(n, V, w, v, c, dp):
    m = 0  # 拆分以后，物品数量就是 m 了，不再是 n
    nw = [0] * (n * 15 + 1)  # 最大拆分数为log2(c[i])
    nv = [0] * (n * 15 + 1)
    for i in range(1, n+1):
        k = 1
        while k < c[i]:
            m += 1
            nw[m] = k * w[i]
            nv[m] = k * v[i]
            c[i] -= k
            k *= 2
        if c[i] > 0:
            m += 1
            nw[m] = c[i] * w[i]
            nv[m] = c[i] * v[i]
    Knapsack01(m, V, nw, nv, dp)

n, V = map(int, input().split())
w = [0] * (n + 1)
v = [0] * (n + 1)
c = [0] * (n + 1)
for i in range(1, n+1):
    w[i], v[i], c[i] = map(int, input().split())

dp = [0] * (V + 1)
KnapsackMultiple(n, V, w, v, c, dp)

ret = 0
for i in range(V + 1):
    ret = opt(ret, dp[i])

print(ret)
