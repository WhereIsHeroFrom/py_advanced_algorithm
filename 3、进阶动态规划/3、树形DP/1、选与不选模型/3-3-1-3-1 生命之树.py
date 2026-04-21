import sys
# Python能过
# PyPy3 无法过
maxn = 100010
sys.setrecursionlimit(maxn)
dp = [[-10**12] * 2 for _ in range(maxn+1)]
child = [[] for _ in range(maxn+1)]
# dp[i][0] 代表以 i 为根节点的子树，且根节点不选的最大价值
# dp[i][1] 代表以 i 为根节点的子树，且根节点选的最大价值

def TreeDPSimple_InitVal(u, isChoose):
    return w[u] if isChoose else 0

def TreeDPSimple_Opt(curVal, isChoose, ncVal, cVal):
    if isChoose:
        return curVal + max(ncVal, cVal)
    return 0

def TreeDPSimple_DFS(u, isChoose, fat):
    if dp[u][isChoose] != -10**12:
        return dp[u][isChoose]
    dp[u][isChoose] = TreeDPSimple_InitVal(u, isChoose)
    for v in child[u]:
        if v == fat:
            continue
        nc = TreeDPSimple_DFS(v, 0, u)
        c = TreeDPSimple_DFS(v, 1, u)
        dp[u][isChoose] = TreeDPSimple_Opt(dp[u][isChoose], isChoose, nc, c)
    return dp[u][isChoose]

n = int(input())
w = [0] + list( map(int, input().split()) )

for _ in range(n-1):
    a, b = map(int, input().split())
    child[a].append(b)
    child[b].append(a)

ans = -10**18
for i in range(1, n+1):
    TreeDPSimple_DFS(i, 0, 0)
    TreeDPSimple_DFS(i, 1, 0)
    ans = max(ans, max(dp[i][0], dp[i][1]))

print(ans)
