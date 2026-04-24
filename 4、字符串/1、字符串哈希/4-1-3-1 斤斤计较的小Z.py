################×Ö·û´®¹þÏ£################
maxn = 1000010
B = 271
mod = 2**64
Power = [0] * maxn
Hash  = [0] * maxn

def init(s):
    Power[0] = 1
    Hash[0] = ord(s[0])
    for i in range(1, len(s)):
        Hash[i] = (Hash[i-1]*B + ord(s[i])) % mod
        Power[i] = (Power[i-1] * B) % mod

def get(l, r):
    if l == 0:
        return Hash[r]
    return (Hash[r] - Hash[l-1]*Power[r-l+1]) % mod

################×Ö·û´®¹þÏ£################

a = input()
b = input()

init(a)
alen = len(a)
v = get(0, alen-1)

init(b)
blen = len(b)
ans = 0
# i+alen-1 < blen
# i < blen-alen+1
# i < n
for i in range(blen-alen+1):
    if get(i, i+alen-1) == v:
        ans += 1
print(ans)
