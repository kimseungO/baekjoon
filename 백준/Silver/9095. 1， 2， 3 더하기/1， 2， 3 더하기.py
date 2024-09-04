t = int(input())

dp=[0] *(11+1)
for i in range(t):
    num = int(input())
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    if num>3:
        for j in range(4, num+1):
            dp[j]=dp[j-1]+dp[j-2]+dp[j-3]
    print(dp[num])