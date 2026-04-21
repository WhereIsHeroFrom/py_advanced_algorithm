# 字符串hash模板
maxn = 1000010
B = 271
mod = 2 ** 64
Power = [0] * maxn
Hash = [0] * maxn

def init(s):
    Power[0] = 1
    Hash[0] = ord(s[0]) % mod
    for i in range(1, len(s)):
        Hash[i] = (Hash[i-1] * B + ord(s[i])) % mod
        Power[i] = (Power[i-1] * B) % mod

def get(l, r):
    # Hash[r] - Hash[l-1] * B ^ {r-l+1}
    if l == 0:
        return Hash[r]
    return (Hash[r] - Hash[l-1] * Power[r - l + 1]) % mod

def check(len_val):
    v = []
    # 1、获取所有长度为 len_val 的子串的哈希值
    for i in range(n - len_val + 1):
        val = get(i, i + len_val - 1)
        v.append( (val, i) )
    # 2、把所有子串的哈希值相等的元素排在一起，并且位置按递增排序
    v.sort()
    # 3、找到所有子串哈希值相等的元素，判断位置是否重叠，如果一旦发现不重叠，返回true
    i = 0
    while i < len(v):
        j = i + 1
        while j < len(v):
            if v[j][0] != v[i][0]:
                i = j - 1
                break
            if v[j][1] - v[i][1] >= len_val:
                return True
            j += 1
        i += 1
    # 4、如果找不到，返回 false
    return False

s = input().strip()
n = len(s)
init(s)

l = -1
r = n // 2 + 1

while l + 1 < r:
    mid = (l + r) // 2
    if check(mid):
        l = mid
    else:
        r = mid

print(l)
