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

def check(sublen):
    v = []
    for i in range(n - sublen + 1):
        val = get(i, i + sublen - 1)
        v.append( (val, i) )
    v.sort()
    i = 0
    while i < len(v):
        j = i + 1
        while j < len(v):
            if v[j][0] != v[i][0]:
                i = j - 1
                break
            if v[j][1] - v[i][1] >= sublen:
                return True
            j += 1
        i += 1
    return False

s = input()
n = len(s)
init(s)

l = -1
r = n//2 + 1
while l + 1 < r:
    mid = (l + r) >> 1
    if check(mid):
        l = mid
    else:
        r = mid
print(l)
