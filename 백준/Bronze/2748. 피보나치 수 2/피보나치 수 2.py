n = int(input())+1

dp = [0] * (n)

dp[0] =0
dp[1] =1
for i in range(2, n):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[-1])