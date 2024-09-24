t = int(input())
for i in range(t):
    n = int(input())
    dp = [1,1,1,2,2]
    if n<5:
        print(dp[n-1])
    else:
        for j in range(5, n):
            dp.append(dp[j-1] + dp[j-5])
        print(dp[n-1])