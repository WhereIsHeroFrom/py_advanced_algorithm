################################分组背包模板################################
inf = -1
init = 0
def opt(a, b):
    if a == inf:
        return b
    if b == inf:
        return a
    return max(a, b)

def KnapsackGroup(n, V, items, dp):
    for i in range(1, V+1):
        dp[0][i] = inf
    dp[0][0] = 0

    for i in range(1, n+1):
        for j in range(V+1):
            # 前i组物品凑出容量为 j 的最优价值
            # dp[i][j] = dp[i-1][j];  代表第 i 组物品可以不选择
            # dp[i][j] = inf;         代表第 i 组物品必须恰好选择1个
            dp[i][j] = dp[i-1][j]
            for k in range(items[i]['cnt']):
                if j >= items[i]['w'][k]:
                    tmp = dp[i-1][j - items[i]['w'][k]] + items[i]['v'][k]
                    dp[i][j] = opt(dp[i][j], tmp)

################################分组背包模板################################

n, V = map(int, input().split())
items = [{} for _ in range(n+1)]

for i in range(1, n+1):
    cnt = int(input())
    w, v = [], []
    for j in range(cnt):
        wi, vi = map(int, input().split())
        w.append(wi)
        v.append(vi)
    items[i]['cnt'] = cnt
    items[i]['w'] = w
    items[i]['v'] = v

dp = [[inf]*(V + 1) for _ in range(n + 1)]
KnapsackGroup(n, V, items, dp)

ret = inf
for i in range(V+1):
    ret = opt(ret, dp[n][i])

print(ret)
