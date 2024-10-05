n = int(input())

dp =[0] * (n+4)
dp[1] =1
dp[2] =2
dp[3] =3

if n>3:
    for i in range(4, n+1):
        n_root = int(i**(1/2))
        sqrlst=[x**2 for x in range(1, n_root+1)]
        chcklst=[]

        for j in sqrlst:
            a=i-j
            chcklst.append(dp[a]+1)
        dp[i]=min(chcklst)
print(dp[n])