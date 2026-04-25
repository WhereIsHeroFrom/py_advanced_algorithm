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

manacher = Manacher()
n, m = map(int, input().split())
s = input()
manacher.manacher(s)

for _ in range(m):
    l, r = map(int, input().split())
    l = 2 * l - 1
    r = 2 * r - 1
    mid = (l + r) // 2
    if mid + manacher.p[mid] - 1 >= r:
        print("Yes")
    else:
        print("No")
