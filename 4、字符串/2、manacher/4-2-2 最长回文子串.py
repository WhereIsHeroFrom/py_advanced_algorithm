# Manacher算法模板
MAXN = 1000010
SPLIT = '$'
p = [0] * MAXN

class Manacher:
    def __init__(self):
        self.str_tmp = ''
    
    def manacher_pre(self, s):
        self.str_tmp = s
        new_str = []
        for i in range(len(self.str_tmp)):
            new_str.append(SPLIT)
            new_str.append(self.str_tmp[i])
        new_str.append(SPLIT)
        return ''.join(new_str)
    
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

manacher = Manacher()
s = input().strip()
ans = manacher.manacher(s)
print(ans // 2)
