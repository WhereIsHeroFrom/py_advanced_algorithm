#################强连通分量(Tarjan算法)#################
class TarjanSCC:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n+1)]
        self.dfn = [0] * (n+1)
        self.low = [0] * (n+1)
        self.inStack = [False] * (n+1)
        self.st = []
        self.timeStamp = 0
        self.sccId = [0] * (n+1)
        self.sccCount = 0
        self.sccNodes = []

    def AddEdge(self, u, v):
        self.adj[u].append(v)
    
    def tarjanDFS(self, u):
        self.timeStamp += 1
        self.dfn[u] = self.timeStamp
        self.low[u] = self.dfn[u]
        self.st.append(u)
        self.inStack[u] = True

        for v in self.adj[u]:
            if self.dfn[v] == 0:
                self.tarjanDFS(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif self.inStack[v]:
                self.low[u] = min(self.low[u], self.dfn[v])

        if self.dfn[u] == self.low[u]:
            scc = []
            while True:
                v = self.st.pop()
                self.inStack[v] = False
                self.sccId[v] = self.sccCount
                scc.append(v)
                if v == u : break
            
            self.sccNodes.append( scc )
            self.sccCount += 1

    def Solve(self):
        for i in range(1, self.n+1):
            if self.dfn[i] == 0:
                self.tarjanDFS(i)
#################强连通分量(Tarjan算法)#################

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    scc = TarjanSCC(n)
    for _ in range(m) :
        u, v = map(int, input().split())
        scc.AddEdge(u, v)
    scc.Solve()

    if scc.sccCount == n:
        print("YES")
    else:
        print("NO")