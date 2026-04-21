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
    parts = list(map(int, input().split()))
    cnt = parts[0]
    w = []
    v = []
    sum_val = 0
    for j in range(cnt):
        x = parts[j+1]
        sum_val += x
        v.append(sum_val)
        w.append(j+1)
    items[i]['cnt'] = cnt
    items[i]['w'] = w
    items[i]['v'] = v

# 初始化dp数组
maxn = 1010
maxv = 2010
dp = [[-1]*(maxv) for _ in range(maxn)]

KnapsackGroup(n, V, items, dp)

ret = -1
for i in range(V+1):
    ret = opt(ret, dp[n][i])

print(ret)
