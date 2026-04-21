import sys

from collections import deque

maxn = 500010
maxd = 18
dummyroot = 0
sys.setrecursionlimit(maxn*maxd)
# 初始化全局变量
f = [[0] * maxd for _ in range(maxn)]  # f[i][j] 代表i号结点的第2^j个祖先
dep = [0] * maxn  # dep[i] 代表i在这棵树上的深度
child = [[] for _ in range(maxn)]
w = [0] * maxn  # w[i] 代表i号结点的零食种类
fw = [[0] * 21 for _ in range(maxn)]  # fw[i][j]代表从根结点到i结点，有多少个种类为j的零食

def LCA_Init(n):
    for i in range(1, n+1):
        child[i].clear()
    # 初始化f数组为dummyroot
    for i in range(maxn):
        for j in range(maxd):
            f[i][j] = dummyroot
    # 初始化fw数组为0
    for i in range(maxn):
        for j in range(21):
            fw[i][j] = 0

def LCA_AddEdge(u, v):
    child[u].append(v)
    child[v].append(u)

def LCA_PreProcess(root):
    q = deque()
    f[root][0] = dummyroot
    fw[root][w[root]] = 1
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
            # 树上前缀和
            for j in range(1, 21):
                fw[v][j] = fw[u][j] + (1 if w[v] == j else 0)
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
w  = [0] + list( map(int, input().split()))

for _ in range(n-1):
    x, y = map(int, input().split())
    LCA_AddEdge(x, y)

LCA_PreProcess(1)

for _ in range(q):
    x, y = map(int, input().split())
    u = LCA_Get(x, y)
    ans = 0
    # 枚举每一种零食，在 x->u 以及 y->u 的路径和上是否出现过
    for j in range(1, 21):
        val = (fw[x][j] - fw[u][j]) + (fw[y][j] - fw[u][j]) + (1 if w[u] == j else 0)
        ans += 1 if val > 0 else 0
    print(ans)
