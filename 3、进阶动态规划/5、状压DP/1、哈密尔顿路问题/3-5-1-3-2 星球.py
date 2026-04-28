import math

############################状压DP模板(哈密尔顿路)############################
maxn = 19
inf = 1000000000
init = 0

# dp[i][j] 代表已经访问了0、2、3三个顶点，且上一个顶点是2的最优解
dp = []
# dis[i][j] 代表从 i->j 的距离
dis = [[0.0 for _ in range(maxn)] for _ in range(maxn)]

# 需要根据实际题目进行修改，有可能是最小值，最大值 或者方案数
def HamiltonDP_opt(curVal, start2i, i2end):
    return min(curVal, start2i + i2end)

# 固定模板，计算任意两点间的距离
def hamiltonDP_initEdges(n, df):
    for i in range(n):
        for j in range(n):
            dis[i][j] = df(i, j)

# 固定模板，初始化所有状态，顶点编号是 [0, n)
def hamiltonDP_Init(n, df):
    for _ in range(1 << n):
        dp.append([-1.0 for _ in range(n)])
    hamiltonDP_initEdges(n, df)

# 固定模板，大部分情况不需要修改
# state ：二进制的1101 代表 0、2、3 三个顶点已经被访问
#     n ：总共多少个顶点
# start : 路径上的起点顶点
#   end ：路径上的终点顶点
def hamiltonDP_Dfs(state, n, start, end):
    if start == end and state == 0:
        return init
    if dp[state][end] >= 0:
        return dp[state][end]
    
    ans = inf
    for i in range(n):
        if (state & (1 << i)) == 0:
            continue
        if (state & (1 << end)) == 0:
            continue
        # start -> ... -> i -> end 为一条路径
        start2i = hamiltonDP_Dfs(state ^ (1 << end), n, start, i)
        i2end = dis[i][end]
        ans = HamiltonDP_opt(ans, start2i, i2end)
    
    dp[state][end] = ans
    return ans

# 固定模板，大部分情况不需要修改
# 求从 start 到 所有的 end 路径上的最优值
def HamiltonDP_Solve(df, n, start):
    hamiltonDP_Init(n, df)
    ret = inf
    for end in range(n):
        ans = hamiltonDP_Dfs((1 << n) - 1, n, start, end)
        ret = HamiltonDP_opt(ret, init, ans)
    return ret

############################状压DP模板(哈密尔顿路)############################
# 这道题目的起点是不固定的，所以可以增加一个点，这个点到所有点距离都为 0
# 从而转换成起点固定的情况

n = int(input()) + 1

x, y, z, w = [0], [0], [0], [0]
for i in range(1, n):
    xi, yi, zi, wi = map(int, input().split())
    x.append(xi)
    y.append(yi)
    z.append(zi)
    w.append(wi)
    
def d(a, b):
    if a == 0:
        return 0
    if b == 0:
        return inf
    ans = (x[a] - x[b]) * (x[a] - x[b])
    ans += (y[a] - y[b]) * (y[a] - y[b])
    ans += (z[a] - z[b]) * (z[a] - z[b])
    return math.sqrt(ans) * w[b]


result = HamiltonDP_Solve(d, n, 0)
print("%.2f" % result)
