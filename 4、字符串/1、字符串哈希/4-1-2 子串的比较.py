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
init(s)
q = int(input())

for _ in range(q):
    l1, r1, l2, r2 = map(int, input().split())
    # 注意：C++中的索引是从0开始的，这里保持一致
    if get(l1, r1) == get(l2, r2):
        print("Yes")
    else:
        print("No")
