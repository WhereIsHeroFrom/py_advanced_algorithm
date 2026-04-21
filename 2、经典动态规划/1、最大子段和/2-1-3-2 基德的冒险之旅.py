def getMSS(n, a, dp):
    # dp[i] 代表以第 i 个数结尾的最大子段和
    ans = -10**18
    dp[0] = 0
    for i in range(1, n+1):
        dp[i] = a[i] + max(dp[i-1], 0)
        ans = max(ans, dp[i])
    # 转换成前 i 个元素的最大子段和
    dp[0] = -10**18
    for i in range(1, n+1):
        dp[i] = max(dp[i], dp[i-1])
    return ans

def swap(n, a):
    for i in range(1, n//2 + 1):
        a[i], a[n+1-i] = a[n+1-i], a[i]

n, k = map(int, input().split())
a = [0] + list(map(int, input().split()))

maxn = 100010
dppre = [0] * maxn
dppost = [0] * maxn

getMSS(n, a, dppre)
swap(n, a)
getMSS(n, a, dppost)
swap(n, dppost)

ans = -10**18
for i in range(1, n - k):
    if i + k + 1 <= n:
        ans = max(ans, dppre[i] + dppost[i + k + 1])

print(ans)
