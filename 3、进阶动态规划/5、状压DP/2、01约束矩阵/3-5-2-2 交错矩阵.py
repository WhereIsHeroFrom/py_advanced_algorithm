####################状压DP模板(带约束的01矩阵)####################
maxn = 21
maxm = 21
inf = 0
init = 1
GridType_EMPTY = -1
GridType_ZERO = 0
GridType_ONE = 1

dp = [[0] * (1 << maxm) for _ in range(2)]
grid = [[0] * maxm for _ in range(maxn)]

# 根据实际题目要求进行修改，有可能是最小值，最大值 或者方案数
def MatrixPutDP_Opt(cur, pre, curOneCount):
    return cur + pre

# 根据实际题目要求进行修改，放置与否
def matrixPutDP_canPut(prestate, curstate, r, c):
    if grid[r][c] != GridType_EMPTY:
        return 0
    # 如果上面有1，不能放1
    if r > 0 and grid[r-1][c] == GridType_ONE:
        return 0
    if prestate & 1:
        return 0

    # 如果左边有1，不能放1
    if c > 0 and grid[r][c-1] == GridType_ONE:
        return 0
    if (curstate >> 1) & 1:
        return 0

    return 1

# 固定模板，无需修改
def MatrixPutDP_Dfs(col, maxcol, 
    row, 
    pre, prestate, 
    cur, curstate, 
    cnt):
    
    if col == maxcol:
        dp[cur][curstate] = MatrixPutDP_Opt(dp[cur][curstate], dp[pre][prestate], cnt)
        return
    # 枚举前一行放和不放
    for i in range(2):
        pres = prestate << 1 | i
        # 枚举这一行放和不放
        for j in range(2):
            curs = (curstate << 1 | j)
            if j == GridType_ONE:
                if not matrixPutDP_canPut(pres, curs, row, col):
                    continue
            MatrixPutDP_Dfs(col+1, maxcol, row, pre, pres, cur, curs, cnt + j)

# 固定模板，无需修改
def MatrixPutDP_Solve(n, m):
    # 1、初始状态
    pre, cur = 0, 1
    for i in range(1 << m):
        dp[pre][i] = inf
    dp[pre][0] = init
    # 2、状态转移
    for i in range(n):
        for j in range(1 << m):
            dp[cur][j] = inf
        MatrixPutDP_Dfs(0, m, i, pre, 0, cur, 0, 0)
        pre, cur = cur, pre
    # 3、总结状态
    ans = inf
    for j in range(1 << m):
        ans = MatrixPutDP_Opt(ans, dp[pre][j], init)
    return ans

####################状压DP模板(带约束的01矩阵)####################

n, m = map(int, input().split())
for i in range(n):
    for j in range(m):
        grid[i][j] = GridType_EMPTY
print(MatrixPutDP_Solve(n, m))