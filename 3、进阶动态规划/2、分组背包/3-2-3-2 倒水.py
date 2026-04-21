def opt(a, b):
    if a == -10**18:
        return b
    if b == -10**18:
        return a
    return max(a, b)

def KnapsackGroup(n, V, items, dp):
    # 初始化
    for i in range(1, V+1):
        dp[0][i] = -10**18
    dp[0][0] = 0

    for i in range(1, n+1):
        for j in range(V+1):
            # 前i组物品凑出容量为j的最优价值
            # 模板稍微改一下，第i个物品不允许不选择的情况
            dp[i][j] = -10**18
            for k in range(items[i]['cnt']):
                if j >= items[i]['w'][k]:
                    tmp = dp[i-1][j - items[i]['w'][k]] + items[i]['v'][k]
                    if dp[i-1][j - items[i]['w'][k]] != -10**18:
                        dp[i][j] = opt(dp[i][j], tmp)

n, V = map(int, input().split())
items = [{} for _ in range(n+1)]

for i in range(1, n+1):
    a, b, c, d, e = map(int, input().split())
    items[i]['cnt'] = 3
    items[i]['w'] = [0, a, c]
    items[i]['v'] = [e, b, d]

# 初始化dp数组
maxn = 1010
maxv = 1010
dp = [[-10**18]*(maxv) for _ in range(maxn)]

KnapsackGroup(n, V, items, dp)

ret = -10**18
for i in range(V+1):
    ret = opt(ret, dp[n][i])

print(ret)
