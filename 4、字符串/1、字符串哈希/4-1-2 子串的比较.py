################×Ö·û´®¹şÏ£################
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

################×Ö·û´®¹şÏ£################

s = input()
init(s)
q = int(input())
while q > 0:
    l1, r1, l2, r2 = map(int, input().split())
    if get(l1, r1) == get(l2, r2) :
        print("Yes\n")
    else:
        print("No\n")
    q -= 1
