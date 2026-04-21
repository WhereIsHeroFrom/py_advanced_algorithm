import sys
sys.setrecursionlimit(1 << 25)

# 求解数据的数据类型
type = int
# 物品的总个数（树的顶点个数）
maxn = 100010
# 总共可以选择的最大容量
maxv = 3

# 物品结构体
items = []
# 树形关系（双向图）
child = [[] for _ in range(maxn)]
# dp[i][j] 代表以i为根的子树中，选择容量总和为j的物品，得到的最优价值
dp = [[0] * maxv for _ in range(maxn)]
# sumVol[i] 代表所有子结点的容量和
sumVol = [0] * maxn
# n件物品，最大容量为V
n, V = 0, 2

# 初始状态值
# 需要根据题目含义进行修改
def KnapsackTree_InitValue(u):
    return 0

# 非法状态值（求最大值时选最小，求最小值时选最大）
# 需要根据题目含义进行修改
def KnapsackTree_InfValue():
    return 1000000000

# 每次状态转移开始时，状态的初始值
# 如果是加边模板，则直接返回 KnapsackTree_InfValue
# 如果是删边模板，则需要根据 v 的值进行判定
def KnapsackTree_CurInitValue(dpu_pre, v):
    if v > 0:
        return dpu_pre[v - 1]
    return KnapsackTree_InfValue()

# 状态转移方程
# 需要根据题目含义进行修改
def KnapsackTree_Opt(curVal, preVal, itemWei):
    return min(curVal, preVal + itemWei)

# 这一步非常关键，目的是把 滚动数组 dpu 中计算出的数据，转移到 dp 上
# dpu 是临时数据，递归结束就销毁了
# dp 是持久化数据，递归结束一直保存
def KnapsackTree_Post(u, dpu):
    for j in range(V + 1):
        dp[u][j] = dpu[j] + items[u].wei

# 获取最优解，根据题目要求执行逻辑
def KnapsackTree_GetAnswer(root):
    ans = KnapsackTree_InfValue()
    for i in range(1, n + 1):
        mv = V if i == root else V - 1
        for j in range(mv + 1):
            ans = KnapsackTree_Opt(ans, dp[i][j], 0)
    return ans

# 模版代码，基本不用改
def KnapsackTree_Init(u):
    dpu = [[0] * maxv for _ in range(2)]
    pre = 0
    dpu[pre][0] = KnapsackTree_InitValue(u)
    for i in range(1, V + 1):
        dpu[pre][i] = KnapsackTree_InfValue()
    return dpu, pre

# 模版代码，基本不用改
def KnapsackTree_DFS(u, fat):
    dpu, pre = KnapsackTree_Init(u)
    cur = 1 - pre
    sumVol[u] = items[u].vol
    for v in child[u]:
        if v == fat:
            continue
        KnapsackTree_DFS(v, u)
        sumVol[u] += sumVol[v]
        for j in range(V + 1):
            dpu[cur][j] = KnapsackTree_CurInitValue(dpu[pre], j)
            for k in range(0, j + 1):
                if k > sumVol[v]:
                    break
                dpu[cur][j] = KnapsackTree_Opt(dpu[cur][j], dpu[pre][j - k], dp[v][k])
        pre, cur = cur, pre
    KnapsackTree_Post(u, dpu[pre])

# 物品类
class Item:
    def __init__(self, vol, wei):
        self.vol = vol
        self.wei = wei

# 主逻辑
V = 2
n = int(input())
items = [Item(0, 0)]  # 占位，索引从1开始
wei = list(map(int, input().split()))
for i in range(0, n):
    items.append(Item(1, wei[i]))

for i in range(n - 1):
    x, y = map(int, input().split())
    child[x].append(y)
    child[y].append(x)

KnapsackTree_DFS(1, 0)
print(KnapsackTree_GetAnswer(1))