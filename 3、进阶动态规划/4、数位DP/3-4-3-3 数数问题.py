maxd = 65

try:
    import sys
    sys.setrecursionlimit(1000000)
except:
    pass

# 一般情况下，1个参数居多，部分情况会有两个参数
# 当需要3个参数的时候，就需要修改这个类了
class DpData:
    K = 0
    base = 0  # 进制
    
    def __init__(self):
        self.data0 = 0  # 所有数字之和
        self.data1 = 0  # 留空不用
        self.init()
    
    def init(self):
        self.data0 = 0
        self.data1 = 0
    
    def dfsReturn(self, is_leadingZero):
        if is_leadingZero:
            # 0000000000
            return 1 if self.K == 0 else 0
        return 1 if self.data0 == self.K else 0
    
    def getNextDpData(self, is_leadingZero, digit):
        ret = DpData()
        ret.data0 = self.data0
        ret.data1 = self.data1
        
        if is_leadingZero:
            # 0000000000
            ret.data0 = digit
        else:
            # 0000122313
            ret.data0 += digit
        
        return ret

# 初始化dp数组
dp = [[[[[-1 for _ in range(2)] for __ in range(305)] for ___ in range(2)] for ____ in range(2)] for _____ in range(maxd)]

def dfs(num, depth, is_leadingZero, is_limit, dpdata):
    if depth == len(num):
        return dpdata.dfsReturn(is_leadingZero)
    
    maxdigit = DpData.base - 1 if is_limit else int(num[depth])
    
    ans = dp[depth][is_leadingZero][is_limit][dpdata.data0][dpdata.data1]
    if ans != -1:
        return ans
    
    ans = 0
    for i in range(0, maxdigit + 1):
        ans += dfs(
            num,
            depth + 1,
            is_leadingZero and (i == 0),
            is_limit or (i < maxdigit),
            dpdata.getNextDpData(is_leadingZero, i)
        )
    
    dp[depth][is_leadingZero][is_limit][dpdata.data0][dpdata.data1] = ans
    return ans

# 固定模板，不需要修改，求 [0, n] 中所有满足条件的数的数量
def getans(n):
    # 重置dp数组
    for i in range(maxd):
        for j in range(2):
            for k in range(2):
                for l in range(305):
                    for m in range(2):
                        dp[i][j][k][l][m] = -1
    
    a = []
    s = []
    
    if n == 0:
        a.append(0)
    else:
        while n:
            a.append(n % DpData.base)
            n //= DpData.base
    
    for i in range(len(a)-1, -1, -1):
        s.append(str(a[i]))
    
    dpd = DpData()
    return dfs(s, 0, True, False, dpd)

# 固定模板，数位DP的差分操作，求 [l, r] 中所有满足条件的数的个数
def getans_range(l, r):
    return getans(r) - getans(l-1)

def solve(a, b, k):
    l = a - 1
    r = b + 1
    lans = getans(a-1)
    
    while l + 1 < r:
        mid = (l + r) // 2
        if getans(mid) - lans >= k:
            r = mid
        else:
            l = mid
    
    if getans(r) - lans >= k:
        return r
    return -1

# 主逻辑
l, r, b, m, k = map(int, input().split())
DpData.base = b
DpData.K = m
ans = solve(l, r, k)

if ans == -1:
    print("No")
else:
    print(ans)
