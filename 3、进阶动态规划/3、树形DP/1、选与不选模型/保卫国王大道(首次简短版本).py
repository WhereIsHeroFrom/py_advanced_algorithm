# dp[i][0] 代表以 i 为根节点的子树，且根节点不选的最小守卫数
# dp[i][1] 代表以 i 为根节点的子树，且根节点选的最小守卫数

inf = 1000000000
dp = []
child = []

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
    dp[u][isChoose] = (1 if isChoose else 0)
    for v in child[u]:
        if v == fat:
            continue
        nc = TreeDPSimple_DFS(v, False, u)
        c = TreeDPSimple_DFS(v, True, u)
        if isChoose:
            dp[u][isChoose] += min(nc, c)
        else:
            dp[u][isChoose] += c
    return dp[u][isChoose]

n = int(input())
TreeDPSimple_Init(n)

for _ in range(n-1):
    a, b = map(int, input().split())
    TreeDPSimple_AddEdge(a, b)

ans = min(
    TreeDPSimple_DFS(1, True, 0),
    TreeDPSimple_DFS(1, False, 0)
)

print(ans)
