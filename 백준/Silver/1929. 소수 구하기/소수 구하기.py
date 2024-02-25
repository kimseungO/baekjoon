M, N=map(int,input().split())

sosu=[False, False] +[True]*(N-1)

alpha=list(range(M, N+1)) # M ~ N의 수
prime=[]
for i in range(2,N+1): #2 ~ N의 소수
    if sosu[i]:
        prime.append(i)
    for j in range(i*2,N+1,i):
        sosu[j]=False
inter=list(set(alpha) & set(prime))
inter.sort()
for i in inter:
    print(i)