import sys
from sys import stdin

mod = 1000000007

# dp[i][0] 代表以 i 为根节点的子树，且根节点不选的方案数
# dp[i][1] 代表以 i 为根节点的子树，且根节点选的方案数

def TreeDPSimple_InitVal(u, isChoose):
    return 1

def TreeDPSimple_Opt(curVal, isChoose, ncVal, cVal):
    if isChoose:
        return curVal * ncVal % mod
    return curVal * (ncVal + cVal) % mod

def TreeDPSimple_Init(n):
    global dp
    dp = [[-1] * 2 for _ in range(n+1)]

def TreeDPSimple_DFS(u, isChoose, fat):
    global dp, child
    if dp[u][isChoose] != -1:
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
    x, y = map(int, stdin.readline().split())
    child[x].append(y)
    child[y].append(x)

ans = (TreeDPSimple_DFS(1, 0, -1) + TreeDPSimple_DFS(1, 1, -1)) % mod

print(ans)
