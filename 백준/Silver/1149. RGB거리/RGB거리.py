n = int(input())

dp=[[0 for x in range(3)] for k in range(n+2)]

for i in range(n):
    rgb=(list(map(int,input().split())))
    if i == 0:
        dp[0] = rgb
    else:
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[2]
print(min(dp[n-1]))