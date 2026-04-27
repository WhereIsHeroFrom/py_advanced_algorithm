##########################################数位DP模板##########################################
import sys
sys.setrecursionlimit(1 << 16)

class DpData:
    # 1、修改点，通过输入数据进行输入
    K = 0
    # 2、修改点，通过题目进行修改，二进制是 2，十进制是 10，也有可能通过输入数据输入
    base = 2
    dp = {}

    def __init__(self):
        self.init()
    
    def init(self):
        # 3、修改点，数据的初始化，确定 data0 和 data1 表示的是什么
        self.data = (
            0,    # 代表二进制表示中 1 的个数
        )
    
    # 4、修改点，修改点，dfs 返回值
    def dfsReturn(self, is_leadingZero):
        if is_leadingZero:
            return 1 if self.K == 0 else 0
        return 1 if self.data[0] == self.K else 0
    
    # 5、修改点，状态转移的过程
    def getNextDpData(self, is_leadingZero, digit):
        ret = DpData()
        ret.data = (
            self.data[0] + (1 if digit == 1 else 0),
        )
        return ret

    # 6、修改点，剪枝，判断是否可以继续枚举
    def isInvalid(self, depth, maxdepth):
        if self.data[0] > K: 
            return True
        if self.data[0] + (maxdepth-depth) < K:
            return True
        return False


# 固定模板，不需要修改，求 [0, n] 中所有满足条件的数的数量
def DigitDP_GetAns(n):

    digits = []
    while n:
        digits.append(n % DpData.base)
        n //= DpData.base
    digits = digits[::-1] if digits else [0]
    dlen = len(digits)
    dpd = DpData()
    DpData.dp = {}

    def digitDP_dfs(
            depth,                  # 当前枚举到的是第几个数位
            is_leadingZero,         # 为 1 时，代表前面枚举的都是0；默认为 1
            is_limit,               # 为 1 时，代表前面数位已经 < num 的高位；默认为 0
            dpdata                  # 数位DP用到的核心数据结构
        ):
        if depth == dlen:
            return dpdata.dfsReturn(is_leadingZero)
        
        if dpdata.isInvalid(depth, dlen):
            return 0
        
        maxdigit = (DpData.base - 1) if is_limit else digits[depth]
        dpstate = (depth, is_leadingZero, is_limit, dpdata.data)
        ans = DpData.dp.get(dpstate, None)
        if ans:
            return ans
        ans = 0
        for i in range(0, maxdigit + 1):
            ans += digitDP_dfs(
                depth + 1,
                is_leadingZero and (i == 0),
                is_limit or (i < maxdigit),
                dpdata.getNextDpData(is_leadingZero, i)
            )
        DpData.dp[dpstate] = ans
        return ans
    
    return digitDP_dfs( 0, True, False, dpd)

# 固定模板，数位DP的差分操作，求 [l, r] 中所有满足条件的数的个数
def DigitDP_GetRange(l, r):
    return DigitDP_GetAns(r) - DigitDP_GetAns(l-1)
##########################################数位DP模板##########################################


# 主逻辑
r, K = map(int, input().split())
DpData.K = K
print(DigitDP_GetRange(1, r))
