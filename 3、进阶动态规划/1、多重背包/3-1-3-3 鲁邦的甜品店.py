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
    nw = [0] * (n * 10 + 1)  # 最大拆分数为log2(c[i])
    nv = [0] * (n * 10 + 1)
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

V, n, c0, d0 = map(int, input().split())
max_items = n + 2
w = [0] * max_items
v = [0] * max_items
c = [0] * max_items

w[1] = c0
c[1] = V // c0
v[1] = d0

for i in range(2, n + 2):
    ai, bi, ci, di = map(int, input().split())
    w[i] = ci
    c[i] = ai // bi
    v[i] = di

dp = [0] * (V + 1)
KnapsackMultiple(n + 1, V, w, v, c, dp)

ret = -1
for i in range(V + 1):
    ret = opt(ret, dp[i])

print(ret)
