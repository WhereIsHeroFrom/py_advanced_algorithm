# ×Ö·û´®hashÄ£°å
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

a = input().strip()
b = input().strip()

init(a)
v = get(0, len(a)-1)
length = len(a)
ans = 0

init(b)
for i in range(len(b) - length + 1):
    if get(i, i + length - 1) == v:
        ans += 1

print(ans)
