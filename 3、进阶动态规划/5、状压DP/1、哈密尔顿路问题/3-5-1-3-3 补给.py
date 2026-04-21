import math

# 状压DP - 哈密尔顿路模板

# 1、第一步：确定 maxn 的大小
maxn = 20
# 2、第二步：确定 type 的类型
type = float
# 3、第三步：确定 dptype 类型
dptype = 0  # 0: MIN, 1: MAX, 2: NUM

# 4、第四步：实现任意两点间距离函数：dis_func
# 5、第五步：调用 HamiltonDP_Solve

# dp[i][j] etc, i = 1101, j = 2
# 代表已经访问了0、2、3三个顶点，且上一个顶点是2的最优解
dp = [[-1 for _ in range(maxn)] for _ in range(1 << maxn)]
# dis[i][j] 代表从 i->j 的距离
dis = [[0.0 for _ in range(maxn)] for _ in range(maxn)]

# 固定模板
def HamiltonDP_opt(a, b, c):
    if dptype == 0:  # MIN
        return min(a, b + c)
    elif dptype == 1:  # MAX
        return max(a, b + c)
    elif dptype == 2:  # NUM
        return a + b * c

# 固定模板，如果类型不是 long long基本不需要修改
def HamiltonDP_ValueInf():
    if dptype == 0:  # MIN
        return 1000000000.0
    elif dptype == 1:  # MAX
        return -1000000000.0
    elif dptype == 2:  # NUM
        return 0.0

# 固定模板
def HamiltonDP_ValueInit():
    if dptype == 0:  # MIN
        return 0.0
    elif dptype == 1:  # MAX
        return 0.0
    elif dptype == 2:  # NUM
        return 1.0

# 固定模板，计算任意两点间的距离
# dis_func 是需要根据实际情况
def HamiltonDP_initEdges(n, df):
    for i in range(n):
        for j in range(n):
            dis[i][j] = df(i, j)

# 固定模板，初始化所有状态
# 顶点编号是 [0, n)
def HamiltonDP_Init(n, df):
    for i in range(1 << n):
        for j in range(n):
            dp[i][j] = -1
    HamiltonDP_initEdges(n, df)

# 固定模板，大部分情况不需要修改
# state ：二进制的1101 代表 0、2、3 三个顶点已经被访问
#     n ：总共多少个顶点
#   pre ：路径上的上一个顶点
def HamiltonDP_Dfs(state, n, isCircle, start, pre):
    if state + 1 == (1 << n):
        init = HamiltonDP_ValueInit()
        inf = HamiltonDP_ValueInf()
        if isCircle:
            return HamiltonDP_opt(inf, init, dis[pre][start])
        return init
    ans = dp[state][pre]
    if ans >= 0:
        return ans
    ans = HamiltonDP_ValueInf()
    for i in range(n):
        if state & (1 << i):
            continue
        d_val = dis[pre][i]
        next_val = HamiltonDP_Dfs(state | (1 << i), n, isCircle, start, i)
        ans = HamiltonDP_opt(ans, d_val, next_val)
    dp[state][pre] = ans
    return ans

def HamiltonDP_Solve(df, n, isCircle, start=-1):
    HamiltonDP_Init(n, df)
    ans = HamiltonDP_ValueInf()
    ini = HamiltonDP_ValueInit()
    if start == -1:
        for i in range(n):
            v = HamiltonDP_Dfs(1 << i, n, isCircle, i, i)
            ans = HamiltonDP_opt(ans, v, ini)
    else:
        v = HamiltonDP_Dfs(1 << start, n, isCircle, start, start)
        ans = HamiltonDP_opt(ans, v, ini)
    return ans

# 具体问题实现
d = [[0.0 for _ in range(maxn)] for _ in range(maxn)]
x = [0] * maxn
y = [0] * maxn

def df(a, b):
    return d[a][b]

n, D = map(int, input().split())
for i in range(n):
    xi, yi = map(int, input().split())
    x[i] = xi
    y[i] = yi

# 初始化距离矩阵
for i in range(n):
    for j in range(n):
        xx = x[i] - x[j]
        yy = y[i] - y[j]
        di = xx * xx + yy * yy
        if di <= D * D:
            d[i][j] = math.sqrt(di)
        else:
            d[i][j] = HamiltonDP_ValueInf()

# Floyd-Warshall算法计算最短路径
for k in range(n):
    for i in range(n):
        for j in range(n):
            if d[i][k] + d[k][j] < d[i][j]:
                d[i][j] = d[i][k] + d[k][j]

result = HamiltonDP_Solve(df, n, True, 0)
print("%.2f" % result)
