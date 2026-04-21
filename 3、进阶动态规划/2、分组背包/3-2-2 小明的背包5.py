def opt(a, b):
    if a == -1:
        return b
    if b == -1:
        return a
    return max(a, b)

def KnapsackGroup(n, V, items, dp):
    # 初始化
    for i in range(1, V+1):
        dp[0][i] = -1
    dp[0][0] = 0

    for i in range(1, n+1):
        for j in range(V+1):
            # 前i组物品凑出容量为j的最优价值
            dp[i][j] = dp[i-1][j]
            for k in range(items[i]['cnt']):
                if j >= items[i]['w'][k]:
                    tmp = dp[i-1][j - items[i]['w'][k]] + items[i]['v'][k]
                    if dp[i-1][j - items[i]['w'][k]] != -1:
                        dp[i][j] = opt(dp[i][j], tmp)

n, V = map(int, input().split())
items = [{} for _ in range(n+1)]

for i in range(1, n+1):
    cnt = int(input())
    w = []
    v = []
    for j in range(cnt):
        wi, vi = map(int, input().split())
        w.append(wi)
        v.append(vi)
    items[i]['cnt'] = cnt
    items[i]['w'] = w
    items[i]['v'] = v

# 初始化dp数组
maxn = 110
maxv = 110
dp = [[-1]*(maxv) for _ in range(maxn)]

KnapsackGroup(n, V, items, dp)

ret = -1
for i in range(V+1):
    ret = opt(ret, dp[n][i])

print(ret)
