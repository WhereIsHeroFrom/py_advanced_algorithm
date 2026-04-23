#############################树形DP(选or不选)模板#############################
inf = 0
dp = []
child = []

def TreeDPSimple_InitVal(u, isChoose):
    return a[u] if isChoose else 0

def TreeDPSimple_Opt(curVal, isChoose, ncVal, cVal):
    if isChoose:
        return curVal + ncVal
    return curVal + max(ncVal, cVal)

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
a = [0] + list(map(int, input().split()))

for _ in range(n-1):
    x, y = map(int, input().split())
    TreeDPSimple_AddEdge(x, y)

ans = max(
    TreeDPSimple_DFS(1, True, 0),
    TreeDPSimple_DFS(1, False, 0)
)

print(ans)
