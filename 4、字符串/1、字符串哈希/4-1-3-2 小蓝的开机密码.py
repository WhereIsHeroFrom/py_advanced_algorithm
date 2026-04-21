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

s = input().strip()
n = len(s)
init(s)

# 1、逆序枚举满足条件的长度，如果发现有一个长度满足条件，直接跳出
l = -1
r = n // 2 + 1

while l + 1 < r:
    i = (l + r) // 2
    check = False
    for j in range(n - 2 * i + 1):
        L = j
        R = j + i - 1
        v = get(L, R)
        for k in range(R + 1, n - i + 1):
            if v == get(k, k + i - 1):
                check = True
                break
        if check:
            break
    if check:
        l = i
    else:
        r = i

print(l)
