# 状压DP - 带约束的01矩阵模板

maxn = 226
maxm = 16
type = int
dptype = 3  # 0: MIN, 1: MAX, 2: NUM, 3: MOD
mod = 10007
MaskType = 15  # Mask::UP|Mask::LEFT|Mask::RIGHT|Mask::DOWN
n, m = 0, 0

# 定义常量
EMPTY = -1
ZERO = 0
ONE = 1
UP = 1 << 0
LEFT = 1 << 1
DOWN = 1 << 2
RIGHT = 1 << 3

# dp[2][1<<maxm]
dp = [[0 for _ in range(1 << maxm)] for _ in range(2)]
grid = [[EMPTY for _ in range(maxm)] for _ in range(maxn)]

# 固定模板
def MatrixPutDP_opt(cur, pre, curOneCount):
    if dptype == 0:  # MIN
        return min(cur, pre + curOneCount)
    elif dptype == 1:  # MAX
        return max(cur, pre + curOneCount)
    elif dptype == 2:  # NUM
        return cur + pre
    else:  # MOD
        return (cur + pre) % mod

# 固定模板，如果类型不是 long long基本不需要修改
def MatrixPutDP_ValueInf():
    if dptype == 0:  # MIN
        return 1000000000
    elif dptype == 1:  # MAX
        return -1000000000
    elif dptype == 2:  # NUM
        return 0
    elif dptype == 3:  # MOD
        return 0

# 固定模板
def MatrixPutDP_ValueInit():
    if dptype == 0:  # MIN
        return 0
    elif dptype == 1:  # MAX
        return 0
    elif dptype == 2:  # NUM
        return 1
    elif dptype == 3:  # MOD
        return 1

# 根据 LEFT 和 UP 进行判断，不能有相邻的 ONE
def MatrixPutDP_canPut(prestate, curstate, r, c):
    if grid[r][c] != EMPTY:
        return False
    if MaskType & UP:
        if r > 0 and grid[r-1][c] == ONE:
            return False
        if prestate & 1:
            return False
    if MaskType & DOWN:
        if r + 1 < n and grid[r+1][c] == ONE:
            return False
    if MaskType & LEFT:
        if c > 0 and grid[r][c-1] == ONE:
            return False
        if (curstate >> 1) & 1:
            return False
    if MaskType & RIGHT:
        if c + 1 < m and grid[r][c+1] == ONE:
            return False
    return True

def MatrixPutDP_Dfs(col, maxcol, row, pre, prestate, cur, curstate, cnt):
    if col == maxcol:
        dp[cur][curstate] = MatrixPutDP_opt(dp[pre][prestate], dp[cur][curstate], cnt)
        return
    # 枚举前一行放和不放
    for i in range(2):
        pres = (prestate << 1) | i
        # 枚举这一行放和不放
        for j in range(2):
            curs = (curstate << 1) | j
            if j == ONE:
                if not MatrixPutDP_canPut(pres, curs, row, col):
                    continue
            MatrixPutDP_Dfs(col + 1, maxcol, row, pre, pres, cur, curs, cnt + j)

def MatrixPutDP_Solve(n, m):
    # 1、初始状态
    pre = 0
    cur = 1
    for i in range(1 << m):
        dp[pre][i] = MatrixPutDP_ValueInf()
    dp[pre][0] = MatrixPutDP_ValueInit()
    # 2、状态转移
    for i in range(n):
        for j in range(1 << m):
            dp[cur][j] = MatrixPutDP_ValueInf()
        MatrixPutDP_Dfs(0, m, i, pre, 0, cur, 0, 0)
        pre, cur = cur, pre
    # 3、总结状态
    ans = MatrixPutDP_ValueInf()
    for j in range(1 << m):
        ans = MatrixPutDP_opt(ans, dp[pre][j], MatrixPutDP_ValueInit())
    return ans

# 主逻辑
n, m = map(int, input().split())
mat = []
for i in range(n):
    line = input().strip()
    mat.append(line)

if n > m:
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '0':
                grid[i][j] = ZERO
            elif mat[i][j] == '1':
                grid[i][j] = ONE
            else:
                grid[i][j] = EMPTY
else:
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '0':
                grid[j][i] = ZERO
            elif mat[i][j] == '1':
                grid[j][i] = ONE
            else:
                grid[j][i] = EMPTY
    n, m = m, n

result = MatrixPutDP_Solve(n, m)
print(result)
