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
n = int(input())
c = []
for _ in range(n):
    line = input()
    c.append(line)
m = n
# 定义方向数组（上、右、下、左）
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 计算节点总数
total_nodes = n * n
hungarian = Hungarian(total_nodes, total_nodes)

# 构建二分图
for i in range(n):
    for j in range(m):
        if c[i][j] == '0':  # 只处理空白格子
            # 将当前格子转换为节点编号
            u = i * m + j + 1
            # 遍历四个方向
            for k in range(4):
                di = i + dir[k][0]
                dj = j + dir[k][1]
                # 检查边界
                if 0 <= di < n and 0 <= dj < m:
                    if c[di][dj] == '0':  # 目标格子也是空白
                        v = di * m + dj + 1
                        hungarian.AddEdge(u, v)

# 计算最大匹配
max_match = hungarian.GetMaxMatch()
# 每个长方形覆盖两个格子，所以结果是最大匹配的一半
print(max_match//2)
