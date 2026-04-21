import sys
from collections import deque

maxn = 500010
maxd = 18
dummyroot = 0

# 初始化全局变量
f = [[0] * maxd for _ in range(maxn)]  # f[i][j] 代表i号结点的第2^j个祖先
dep = [0] * maxn  # dep[i] 代表i在这棵树上的深度
child = [[] for _ in range(maxn)]

def LCA_Init(n):
    for i in range(1, n+1):
        child[i].clear()
    # 初始化f数组为dummyroot
    for i in range(maxn):
        for j in range(maxd):
            f[i][j] = dummyroot

def LCA_AddEdge(u, v):
    child[u].append(v)
    child[v].append(u)

def LCA_PreProcess(root):
    q = deque()
    f[root][0] = dummyroot
    dep[root] = 0
    q.append(root)
    
    while q:
        u = q.popleft()
        for i in range(1, maxd):
            f[u][i] = f[f[u][i-1]][i-1]
            if f[u][i] == dummyroot:
                break
        for v in child[u]:
            if v == f[u][0]:
                continue
            f[v][0] = u
            dep[v] = dep[u] + 1
            q.append(v)

def LCA_Get(u, v):
    # 确保 u的深度 >= v的深度
    if dep[u] < dep[v]:
        return LCA_Get(v, u)
    # 将 u 和 v 调整到同一深度
    for i in range(maxd-1, -1, -1):
        if dep[u] - (1 << i) >= dep[v]:
            u = f[u][i]
    if u == v:
        return u
    # 让 u 和 v 同时网上进行倍增
    for i in range(maxd-1, -1, -1):
        if f[u][i] != f[v][i]:
            u = f[u][i]
            v = f[v][i]
    return f[u][0]

# 主逻辑
n, q = map(int, input().split())
LCA_Init(n)

for _ in range(n-1):
    x, y = map(int, input().split())
    LCA_AddEdge(x, y)

LCA_PreProcess(1)

for _ in range(q):
    x, y = map(int, input().split())
    print(LCA_Get(x, y))
