##############LIS模板##############
# a[i]  < g[mid] 时，求不降
# a[i] <= g[mid] 时，求递增
def getLIS(n, a, dp):
    # g[i] 代表长度为 i 的
    # 最长递增子序列的最后一个数是什么
    g = []
    gSize = 0
    for i in range(n):
        # 二分查找找到插入位置
        l = -1
        r = gSize
        while l + 1 < r:
            mid = (l + r) // 2
            if a[i] < g[mid]:
                r = mid
            else:
                l = mid
        # l + 1 == r
        if r == gSize:
            g.append(a[i])
            gSize += 1
        else:
            g[r] = a[i]
        dp[i] = gSize
    return gSize
##############LIS模板##############

def swap(a):
    a[:] = a[::-1]

n = int(input())
a = list(map(int, input().split()))
dppre, dppost = [0] * n, [0] * n

getLIS(n, a, dppre)
swap(a)
getLIS(n, a, dppost)
swap(dppost)

ans = 0
for i in range(n):
    ans = max(ans, dppre[i] + dppost[i] - 1)

print(n - ans)
