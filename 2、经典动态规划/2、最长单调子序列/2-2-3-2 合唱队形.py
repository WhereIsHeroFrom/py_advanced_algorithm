def getLIS(n, a, dp):
    # g[i] 代表长度为 i 的最长递增子序列的最后一个数是什么
    g = []
    gSize = 0
    for i in range(n):
        # 二分查找找到插入位置
        l = -1
        r = gSize
        while l + 1 < r:
            mid = (l + r) // 2
            if a[i] <= g[mid]:
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

def swap(n, a):
    for i in range(n//2):
        a[i], a[n-1-i] = a[n-1-i], a[i]

n = int(input())
a = list(map(int, input().split()))

dppre = [0] * n
dppost = [0] * n

getLIS(n, a, dppre)
swap(n, a)
getLIS(n, a, dppost)
swap(n, dppost)

ans = 0
for i in range(n):
    ans = max(ans, dppre[i] + dppost[i] - 1)

print(n - ans)
