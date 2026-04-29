################################# 树上分组背包模板 ###############################
maxn = 5010
maxv = 5010
inf = 1000000000

class Item:
    def __init__(self):
        self.vol = 0    # 每个物品的容量
        self.wei = 0    # 每个物品的权值
        self.edge = 0   # 每个物品的边权

items = [Item() for _ in range(maxn)]
edges = [[] for _ in range(maxn)]

# dp[i][j] 代表以i为根的子树中
# 想要得到 j 个气球的最小力气
dp = [[inf] * maxv for _ in range(maxn)]
# sumVol[i] 代表所有子结点的容量和
sumVol = [0] * maxn
# n件物品，最大容量为V
n, V = 0, 0

# 1、修改点，初始状态值
# 需要根据题目含义进行修改
def KnapsackTreeDP_InitValue(u):
    return 0

# 2、修改点，状态转移方程
# 需要根据题目含义进行修改
def KnapsackTreeDP_Opt(curVal, preVal, itemWei):
    return min(curVal, preVal + itemWei)

# 3、修改点，这一步非常关键
# 目的是把 滚动数组 dpu 中计算出的数据，转移到 dp 上
# dpu 是临时数据，递归结束就销毁了
# dp 是持久化数据，递归结束一直保存
def KnapsackTreeDP_Post(u, dpu):
    for j in range(0, V + 1):
        dp[u][j] = dpu[j]
    # 割断绳子
    dp[u][ sumVol[u] ] = KnapsackTreeDP_Opt(dp[u][ sumVol[u] ], items[u].edge, 0)
    # 戳破气球
    dp[u][ sumVol[u]-1 ] = KnapsackTreeDP_Opt(dp[u][ sumVol[u]-1 ], items[u].wei, 0)

# 4、修改点，获取最优解，根据题目要求执行逻辑
def KnapsackTreeDP_GetAnswer(root, w):
    ans = inf
    for i in range(n, -1, -1):
        if dp[root][i] <= w:
            return i
    return ans

# 模版代码，基本不用改
def KnapsackTreeDP_Dfs(u, fat):
    # 1、初始化 dpu[pre][...]
    dpu = [[inf] * (V + 1) for _ in range(2)]
    pre, cur = 0, 1
    dpu[pre][0] = KnapsackTreeDP_InitValue(u)
    for i in range(1, V + 1):
        dpu[pre][i] = inf
    sumVol[u] = items[u].vol
    # 2、遍历子结点进行分组背包
    for v in edges[u]:
        if v == fat:
            continue
        KnapsackTreeDP_Dfs(v, u)
        sumVol[u] += sumVol[v]
        for j in range(0, V + 1):
            # 以 u 为根的子树中，在总容量为 j 的情况下
            # 选择容量总和为 j 的物品，得到的最优价值
            # k 代表 v 子结点中选择的物品容量总和
            # j-k 代表在 v 之前的子结点中选择的物品容量总和
            dpu[cur][j] = inf
            k = 0
            while k <= j and k <= sumVol[v]:
                dpu[cur][j] = KnapsackTreeDP_Opt(dpu[cur][j], dpu[pre][j - k], dp[v][k])
                k += 1
        pre, cur = cur, pre
    # 3、把 滚动数组 dpu 中计算出的数据，转移到 dp 上
    KnapsackTreeDP_Post(u, dpu[pre])
################################# 树上分组背包模板 ###############################

n, w = map(int, input().split())
V = n
wei = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    items[i].vol = 1
    items[i].wei = wei[i]

items[1].edge = inf
for i in range(1, n):
    x, y = map(int, input().split())
    edges[x].append(i + 1)  
    items[i + 1].edge = y

KnapsackTreeDP_Dfs(1, 0)
print(KnapsackTreeDP_GetAnswer(1, w))
