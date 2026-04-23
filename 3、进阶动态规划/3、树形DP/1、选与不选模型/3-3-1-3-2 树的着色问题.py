mod = 1000000007
#############################树形DP(选or不选)模板#############################
inf = -1
dp = []
child = []

def TreeDPSimple_InitVal(u, isChoose):
    return 1

def TreeDPSimple_Opt(curVal, isChoose, ncVal, cVal):
    if isChoose:
        return curVal * ncVal % mod
    return curVal * (ncVal + cVal) % mod

def TreeDPSimple_Init(n):
    for _ in range(n+1):
        child.append([])
        dp.append( [ inf ] * 2 )

def TreeDPSimple_AddEdge(u, v):
    child[u].append(v)
    child[v].append(u)

def TreeDPSimple_DFS(u, isChoose, fat):
    if dp[u][isChoose] != inf:
        return dp[u][isChoose]
    dp[u][isChoose] = TreeDPSimple_InitVal(u, isChoose)
    for v in child[u]:
        if v == fat:
            continue
        nc = TreeDPSimple_DFS(v, False, u)
        c = TreeDPSimple_DFS(v, True, u)
        dp[u][isChoose] = TreeDPSimple_Opt(dp[u][isChoose], isChoose, nc, c)
    return dp[u][isChoose]
#############################树形DP(选or不选)模板#############################


n = int(input())
TreeDPSimple_Init(n)

for _ in range(n-1):
    x, y = map(int, input().split())
    TreeDPSimple_AddEdge(x, y)

ans = (TreeDPSimple_DFS(1, 0, -1) + TreeDPSimple_DFS(1, 1, -1)) % mod
print(ans)
