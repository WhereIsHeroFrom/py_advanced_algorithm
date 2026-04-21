def opt(a, b):
    if a == "":
        return b
    if b == "":
        return a
    if len(a) == len(b):
        return a if a > b else b
    return a if len(a) > len(b) else b

def KnapsackGroup(n, V, items, dp):
    # 初始化
    for i in range(1, V+1):
        dp[0][i] = ""
    dp[0][0] = ""

    for i in range(1, n+1):
        for j in range(V+1):
            # 前i组物品凑出容量为j的最优价值
            dp[i][j] = dp[i-1][j]
            for k in range(items[i]['cnt']):
                if j >= items[i]['w'][k]:
                    remaining = j - items[i]['w'][k]
                    if remaining == 0 or dp[i-1][remaining] != "":
                        tmp = dp[i-1][remaining] + items[i]['v'][k]
                        dp[i][j] = opt(dp[i][j], tmp)

n = 9
V = 300
tbl = [-1, 2, 5, 5, 4, 5, 6, 3, 7, 6]

items = [{} for _ in range(n+1)]

for i in range(1, n+1):
    items[i]['cnt'] = 10
    num = n + 1 - i
    w = []
    v = []
    for j in range(items[i]['cnt']):
        w.append(tbl[num] * (j + 1))
        # 生成重复num j+1次的字符串
        v.append(str(num) * (j + 1))
    items[i]['w'] = w
    items[i]['v'] = v

# 初始化dp数组
maxn = 10
maxv = 305
dp = [[""]*(maxv) for _ in range(maxn)]

KnapsackGroup(n, V, items, dp)

ret = ""
for i in range(V+1):
    ret = opt(ret, dp[n][i])

print(ret)
