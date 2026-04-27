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

#################强连通分量(缩图算法)###################

class DAG:
    def __init__(self):
        self.n = 0
        self.adj = []
        self.ind = []
        self.outd = []
    
    def init(self, sccCount):
        self.n = sccCount
        self.adj = [ set() for _ in range(sccCount) ]
        self.ind = [ 0 ] * sccCount
        self.outd = [ 0 ] * sccCount
    def addEdge(self, u, v):
        if u == v:
            return
        if v not in self.adj[u]:
            self.adj[u].add(v)
            self.outd[u] += 1
            self.ind[v] += 1

    def Build(self, scc):
        self.init(scc.sccCount)
        for i in range(scc.sccCount):
            com = scc.sccNodes[i]
            for u in com:
                # (u, v)
                for v in scc.adj[u]:
                    self.addEdge(i, scc.sccId[v])
#################强连通分量(缩图算法)###################
def Solve(dag):
    if dag.n == 1:
        return 0
    ind = 0
    outd = 0
    for i in range(dag.n):
        if dag.ind[i] == 0: ind += 1
        if dag.outd[i] == 0: outd += 1
    return max(ind, outd)
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    scc = TarjanSCC(n)
    for _ in range(m):
        u, v = map(int, input().split())
        scc.AddEdge(u, v)
    scc.Solve()
    dag = DAG()
    dag.Build(scc)
    print(Solve(dag))
