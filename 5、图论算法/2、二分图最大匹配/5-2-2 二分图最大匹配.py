#######################二分图最大匹配(匈牙利算法)#######################
class Hungarian:
    def __init__(self, n, m):
        self.n = n                             # 左部节点数
        self.m = m                             # 右部节点数
        self.adj = [[] for _ in range(n + 1)]  # 邻接表
        self.pre = [-1] * (m + 1)              # 右部节点匹配的左部节点
    
    def findMatch(self, u, visit):
        for v in self.adj[u]:
            if not visit[v]:
                visit[v] = True
                vpre = self.pre[v]
                self.pre[v] = u
                if vpre == -1 or self.findMatch(vpre, visit):
                    return True
                self.pre[v] = vpre
        return False

    def AddEdge(self, u, v):
        self.adj[u].append(v)

    def GetMaxMatch(self):
        cnt = 0
        for i in range(1, self.n + 1):
            visit = [False] * (self.m + 1)
            if self.findMatch(i, visit):
                cnt += 1
        return cnt
    
#######################二分图最大匹配(匈牙利算法)#######################

# 主逻辑
n, m, e = map(int, input().split())
hungarian = Hungarian(n, m)
for _ in range(e):
    u, v = map(int, input().split())
    hungarian.AddEdge(u, v)

print(hungarian.GetMaxMatch())
