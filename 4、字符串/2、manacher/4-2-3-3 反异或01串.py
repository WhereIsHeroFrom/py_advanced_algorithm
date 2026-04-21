# Manacher算法模板
MAXN = 2000010
SPLIT = '$'
p = [0] * MAXN

class Manacher:
    def __init__(self):
        self.str_tmp = ''
        self.processed_str = ''
    
    def manacher_pre(self, s):
        self.str_tmp = s
        new_str = []
        for i in range(len(self.str_tmp)):
            new_str.append(SPLIT)
            new_str.append(self.str_tmp[i])
        new_str.append(SPLIT)
        self.processed_str = ''.join(new_str)
        return self.processed_str
    
    def manacher_match(self, a, b):
        return a == b
    
    def manacher(self, s):
        s = self.manacher_pre(s)
        # ct: 当前已知最右回文区域的中心位置
        # r: 当前已知最右回文区域的右边界（即ct + p[ct]）
        # p[]: 记录每个位置的回文半径
        ct = 0
        r = 0
        max_len = 1
        p[0] = 1
        
        for i in range(1, len(s)):
            # 1.计算p[i]初始值
            if i < r:
                p[i] = min(p[2*ct - i], r - i)
            else:
                p[i] = 0
            
            # 2.扩张p[i]，以适应达到p[i]最大值
            while i - p[i] >= 0 and i + p[i] < len(s) and self.manacher_match(s[i - p[i]], s[i + p[i]]):
                p[i] += 1
            
            # 3.更新ct
            if p[i] + i > r:
                ct = i
                r = p[i] + i
            
            # 4.更新最长回文
            if 2 * p[i] - 1 > max_len:
                max_len = 2 * p[i] - 1
        
        return max_len

def getsum(sum_arr, l, r):
    pre = 0
    if l > 0:
        pre = sum_arr[l-1]
    return sum_arr[r] - pre

manacher = Manacher()
s = input().strip()
manacher.manacher(s)

processed_str = manacher.processed_str
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
    # 再统计这个回文串 [i-p[i]+1, i+p[i]-1] 以外1的个数
    ans = getsum(sum_arr, i, i + p[i] - 1) + getsum(sum_arr, 0, n-1) - getsum(sum_arr, i - p[i] + 1, i + p[i] - 1)
    ret = min(ret, ans)

print(ret)
