################################Manacher算法模板################################
class Manacher:
    SPLIT = '$'
    def __init__(self):
        # p[]: 每个位置的回文半径
        # ct: 当前已知最右回文区域的中心位置
        # r: 当前已知最右回文区域的右边界（即ct + p[ct]）
        self.p = []
        self.ct = 0
        self.r = 0
        self.str_tmp = ''
        self.str_processed = ''
    
    def manacher_pre(self, s):
        self.str_tmp = s
        new_str = []
        for i in range(len(self.str_tmp)):
            new_str.append(self.SPLIT)
            new_str.append(self.str_tmp[i])
        new_str.append(self.SPLIT)
        new_str = ''.join(new_str)
        self.p = [0] * len(new_str)
        return new_str
    
    def manacher_match(self, a, b):
        return a == b
    
    def manacher(self, s):
        self.str_processed = self.manacher_pre(s)
        max_len = 1
        self.p[0] = 1
        
        for i in range(1, len(self.str_processed)):
            # 1.计算p[i]初始值
            if i < self.r:
                self.p[i] = min(self.p[2*self.ct - i], self.r - i)
            else:
                self.p[i] = 0
            
            # 2.扩张p[i]，以适应达到p[i]最大值
            while i - self.p[i] >= 0 and i + self.p[i] < len(self.str_processed):
                if not self.manacher_match(
                    self.str_processed[i - self.p[i]], 
                    self.str_processed[i + self.p[i]]
                ):
                    break
                self.p[i] += 1
            
            # 3.更新ct
            if self.p[i] + i > self.r:
                self.ct = i
                self.r = self.p[i] + i
            
            # 4.更新最长回文
            if 2 * self.p[i] - 1 > max_len:
                max_len = 2 * self.p[i] - 1
        
        return max_len

################################Manacher算法模板################################


'''
1、由于反异或操作只能进行最多一次，所以我们就可以挑选其中一段来进行反异或操作，
而剩下的段，统计 1 的个数就可以了，于是问题就转变成了 "如何找到需要反异或操作的段"；

2、考虑这种情况，先考虑奇数的情况：
a  b  c  d  e
^  ^  ^  ^  ^
e  d  c  b  a
满足可以反异或的前提：中间这个位置必须是 0，因为自己异或自己必然是 0
然后由于异或满足交换律，也就是 b^d == d^b，所以就变成了求回文串的过程了；
同样偶数也是一样的，只不过偶数不需要判断中间位置是 0 的情况；

3、利用 manacher 计算出每个位置作为回文串中心的最大半径 p[i]，
并且求 区间中[ i, i+p[i]-1 ] 中 1 的个数，代表 反异或 操作之前需要的 1
再求区间 [i-p[i]+1, i+p[i]-1] 以外的1 的个数代表不进行反异或操作的段中需要的 1；
把两者累加即可；
'''

def getsum(sum_arr, l, r):
    pre = 0
    if l > 0:
        pre = sum_arr[l-1]
    return sum_arr[r] - pre

manacher = Manacher()
s = input().strip()
manacher.manacher(s)

processed_str = manacher.str_processed
n = len(processed_str)

# 计算前缀和
sum_arr = [0] * n
for i in range(1, n):
    sum_arr[i] = sum_arr[i-1] + (1 if processed_str[i] == '1' else 0)

ret = sum_arr[n-1]

for i in range(n):
    if i % 2 == 1:
        # 奇数位置，以数字为中心
        if processed_str[i] == '1':
            # 中间数不可能为 1，因为自己异或自己一定是 0
            continue
    else:
        # 偶数位置，以 '$' 为中心
        pass
    
    # 统计 [i, i+p[i]-1] 的 1 的个数
    ans = getsum(sum_arr, i, i + manacher.p[i] - 1) 
    # 再统计这个回文串 [i-p[i]+1, i+p[i]-1] 以外1的个数
    ans += getsum(sum_arr, 0, n-1) 
    ans -= getsum(sum_arr, i - manacher.p[i] + 1, i + manacher.p[i] - 1)
    ret = min(ret, ans)

print(ret)
