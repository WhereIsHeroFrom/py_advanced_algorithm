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

n = int(input())
a = [0] + list(map(int, input().split()))

maxn = 2010
dp = [[0]*(maxn) for _ in range(maxn)]

for i in range(1, n+1):
    # 构建子数组 a[i...n]
    sub_a = [0] * (n - i + 2)
    for j in range(1, n - i + 2):
        sub_a[j] = a[i + j - 1]
    getMSS(n - i + 1, sub_a, dp[i])

t = int(input())
while t > 0:
    t -= 1
    l, r = map(int, input().split())
    print(dp[l][r - l + 1])
