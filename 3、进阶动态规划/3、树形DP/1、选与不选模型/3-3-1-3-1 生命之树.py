import sys
sys.setrecursionlimit(200000)

#############################树形DP(选or不选)模板#############################
inf = -10**12
dp = []
child = []

def TreeDPSimple_InitVal(u, isChoose):
    return w[u] if isChoose else 0

def TreeDPSimple_Opt(curVal, isChoose, ncVal, cVal):
    if isChoose:
        return curVal + max(ncVal, cVal)
    return 0

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

w = [0] + list( map(int, input().split()) )

for _ in range(n-1):
    a, b = map(int, input().split())
    TreeDPSimple_AddEdge(a, b)

ans = inf
for i in range(1, n+1):
    TreeDPSimple_DFS(i, 0, 0)
    TreeDPSimple_DFS(i, 1, 0)
    ans = max(ans, max(dp[i][0], dp[i][1]))

print(ans)
