######################多重背包模板######################
inf = -1
init = 0
def opt(a, b):
    if a == inf:
        return b
    if b == inf:
        return a
    return max(a, b)

def Knapsack01(n, V, w, v, dp):
    for i in range(1, V+1):
        dp[i] = inf
    dp[0] = init
    for i in range(1, n+1):
        for j in range(V, w[i]-1, -1):
            if dp[j - w[i]] != inf:
                dp[j] = opt(dp[j], dp[j - w[i]] + v[i])

def KnapsackMultiple(n, V, w, v, c, dp):
    nw, nv = [0], [0]
    for i in range(1, n+1):
        k = 1
        while k < c[i]:
            nw.append(k * w[i])
            nv.append(k * v[i])
            c[i] -= k
            k *= 2
        if c[i] > 0:
            nw.append(c[i] * w[i])
            nv.append(c[i] * v[i])
    Knapsack01(len(nw)-1, V, nw, nv, dp)
######################多重背包模板######################


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
