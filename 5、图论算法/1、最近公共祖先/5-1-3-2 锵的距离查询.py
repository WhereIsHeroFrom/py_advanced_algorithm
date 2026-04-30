#######################最近公共祖先(倍增算法)#######################
from collections import deque

maxd = 18
dummyroot = 0

class LCA:
    def __init__(self):
        self.f = []           # f[i][j] 代表i号结点的第2^j个祖先
        self.dep = []         # dep[i] 代表i在这棵树上的深度
        self.adj = []
        self.q = None
        self.n = 0            # 树的总结点数

    def Initialize(self, n):
        self.n = n
        self.adj = [[] for _ in range(n + 1)]
        self.dep = [0] * (n + 1)
        self.f = [[dummyroot] * maxd for _ in range(n + 1)]

    def AddEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def PreProcess(self, root):
        self.q = deque()
        self.f[root][0] = dummyroot
        self.dep[root] = 0
        self.q.append(root)

        while self.q:
            u = self.q.popleft()
            for i in range(1, maxd):
                self.f[u][i] = self.f[self.f[u][i-1]][i-1]
                if self.f[u][i] == dummyroot:
                    break
            for v in self.adj[u]:
                if v == self.f[u][0]:
                    continue
                self.f[v][0] = u
                self.dep[v] = self.dep[u] + 1
                self.q.append(v)

    def Get(self, u, v):
        # 1、确保 u的深度 >= v的深度
        if self.dep[u] < self.dep[v]:
            return self.Get(v, u)
        # 2、将 u 和 v 调整到同一深度
        for i in range(maxd-1, -1, -1):
            if self.dep[u] - (1 << i) >= self.dep[v]:
                u = self.f[u][i]
        if u == v:
            return u
        # 3、让 u 和 v 同时往上进行倍增
        for i in range(maxd-1, -1, -1):
            if self.f[u][i] != self.f[v][i]:
                u = self.f[u][i]
                v = self.f[v][i]
        return self.f[u][0]
    
#######################最近公共祖先(倍增算法)#######################
lca = LCA()
n, q = map(int, input().split())
lca.Initialize(n)

for _ in range(n-1):
    x, y = map(int, input().split())
    lca.AddEdge(x, y)

lca.PreProcess(1)

for _ in range(q):
    x, y = map(int, input().split())
    z = lca.Get(x, y)
    print((lca.dep[x] - lca.dep[z]) + (lca.dep[y] - lca.dep[z]))
