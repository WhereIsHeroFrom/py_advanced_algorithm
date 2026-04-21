import sys
from sys import stdin

# dp[i][0] 代表以 i 为根节点的子树，且根节点不选的最小守卫数
# dp[i][1] 代表以 i 为根节点的子树，且根节点选的最小守卫数

def TreeDPSimple_InitVal(u, isChoose):
    return 1 if isChoose else 0

def TreeDPSimple_Opt(curVal, isChoose, ncVal, cVal):
    if isChoose:
        return curVal + min(ncVal, cVal)
    return curVal + cVal

def TreeDPSimple_Init(n):
    global dp
    dp = [[float('inf')] * 2 for _ in range(n+1)]

def TreeDPSimple_DFS(u, isChoose, fat):
    global dp, child
    if dp[u][isChoose] != float('inf'):
        return dp[u][isChoose]
    dp[u][isChoose] = TreeDPSimple_InitVal(u, isChoose)
    for v in child[u]:
        if v == fat:
            continue
        nc = TreeDPSimple_DFS(v, False, u)
        c = TreeDPSimple_DFS(v, True, u)
        dp[u][isChoose] = TreeDPSimple_Opt(dp[u][isChoose], isChoose, nc, c)
    return dp[u][isChoose]

n = int(stdin.readline())
child = [[] for _ in range(n+1)]

TreeDPSimple_Init(n)

for _ in range(n-1):
    a, b = map(int, stdin.readline().split())
    child[a].append(b)
    child[b].append(a)

ans = min(
    TreeDPSimple_DFS(1, True, 0),
    TreeDPSimple_DFS(1, False, 0)
)

print(ans)
