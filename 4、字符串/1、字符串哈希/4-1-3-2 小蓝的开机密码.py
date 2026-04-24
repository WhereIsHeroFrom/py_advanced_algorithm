######################×Ö·û´®hashÄ£°å######################
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

######################×Ö·û´®hashÄ£°å######################

def check(s, slen, sublen):
    for j in range(slen - 2 * sublen + 1):
        l = j
        r = j + sublen - 1
        v = get(l, r)
        for k in range(r + 1, slen - sublen + 1):
            if v == get(k, k + sublen - 1):
                return True
    return False

s = input()
n = len(s)
init(s)

l = -1
r = n // 2 + 1
while l + 1 < r:
    mid = (l + r) // 2
    if check(s, n, mid):
        l = mid
    else:
        r = mid

print(l)
