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
        if a == b:
            return a == self.SPLIT
        return (int(a) + int(b)) == 1
    
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
1、首先，满足要求的子串一定是偶数长度的。
反证法证明，假设是奇数，如下：
原串： a    b    c
取反：1-a  1-b  1-c
反转：1-c  1-b  1-a
你会发现，要求 b == 1-b，显然是不合理的，所以可得，原串必为偶数。
2、于是，同样的方法， 观察偶数情况：
原串： a    b    c    d
取反：1-a  1-b  1-c  1-d
反转：1-d  1-c  1-b  1-a
得出结论：a+d==1   b+c==1
3、这样一来，只需要把原先的 马拉车 模板，两边字符相等的逻辑，改成字符相加等于1即可
4、最后统计这样的偶数串的个数，做简单的计数操作即可
偶数串的中心位置一定是$，所以p[i] // 2 就是偶数串的个数
'''


manacher = Manacher()
n = int(input())
s = input()
manacher.manacher(s)

ans = 0
for i in range(0, len(manacher.str_processed), 2):
    ans += manacher.p[i] // 2

print(ans)
