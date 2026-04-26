######################强连通分量(Tarjan算法)######################

class TarjanSCC:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n + 1)]  # 邻接表
        self.dfn = [0] * (n + 1)  # 节点的发现时间
        self.low = [0] * (n + 1)  # 节点能到达的最早节点的发现时间
        self.inStack = [False] * (n + 1)  # 节点是否在栈中
        self.st = []  # 栈，用于维护强连通分量
        self.timeStamp = 0  # 时间戳
        self.sccId = [0] * (n + 1)  # 每个节点所属的强连通分量编号
        self.sccCount = 0  # 强连通分量的数量
        self.sccNodes = []  # 存储每个强连通分量的节点
    
    def addEdge(self, u, v):
        self.adj[u].append(v)
    
    def tarjanDFS(self, u):
        self.timeStamp += 1
        self.dfn[u] = self.low[u] = self.timeStamp
        self.st.append(u)
        self.inStack[u] = True
        
        for v in self.adj[u]:
            if self.dfn[v] == 0:  # 未被访问过
                self.tarjanDFS(v)
                self.low[u] = min(self.low[u], self.low[v])
            elif self.inStack[v]:  # 已被访问过且在栈中
                self.low[u] = min(self.low[u], self.dfn[v])
        
        # 找到强连通分量的根节点
        if self.dfn[u] == self.low[u]:
            scc = []
            while True:
                v = self.st.pop()
                self.inStack[v] = False
                self.sccId[v] = self.sccCount
                scc.append(v)
                if v == u:
                    break
            self.sccNodes.append(scc)
            self.sccCount += 1
    
    def solve(self):
        for i in range(1, self.n + 1):
            if self.dfn[i] == 0:
                self.tarjanDFS(i)
    
    def getSCCCount(self):
        return self.sccCount
    
    def getSCCId(self, u):
        return self.sccId[u]
    
    def getSCCNodes(self, sccId):
        return self.sccNodes[sccId]
    
######################强连通分量(Tarjan算法)######################


# 主逻辑
n, m = map(int, input().split())
scc = TarjanSCC(n)
for _ in range(m):
    u, v = map(int, input().split())
    scc.addEdge(u, v)
scc.solve()

# 输出结果
print(scc.getSCCCount())
ret = []
for i in range(scc.getSCCCount()):
    nodes = scc.getSCCNodes(i)
    min_node = min(nodes)
    ret.append(min_node)
ret.sort()
for node in ret:
    print(node, end='\n')
