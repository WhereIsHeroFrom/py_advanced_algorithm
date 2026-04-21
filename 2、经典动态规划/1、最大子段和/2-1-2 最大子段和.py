#############最大子数组和模板#############
# a列表的第0个元素是不用的，从第1个元素开始
def getMSS(n, a, dp):
    # dp[i] 代表以第 i 个数结尾的最大子段和
    dp[0] = 0
    for i in range(1, n+1):
        dp[i] = a[i] + max(dp[i-1], 0)
    # 转换成前 i 个元素的最大子段和
    dp[0] = -10**18
    for i in range(1, n+1):
        dp[i] = max(dp[i], dp[i-1])
    return dp[n]
#############最大子数组和模板#############

n = int(input())
a = [0] + list(map(int, input().split()))
dp = [0] * len(a)
print(getMSS(n, a, dp))
