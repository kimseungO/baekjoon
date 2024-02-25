Number=[]
while True:
    Nm=int(input())
    if Nm==0:
        break
    else:
        Number.append(Nm)
prime=[]
def sosunumber(N    ):
    sosu=[False, False] +[True]*((2*N)-1)

    for i in range(2,(2*N)+1): 
        if sosu[i]:
            prime.append(i)
        for j in range(i*2,(2*N)+1,i):
            sosu[j]=False
sosunumber(max(Number))
for N in Number:
    alpha=list(range(N+1, (2*N)+1)) 
    inter=list(set(alpha) & set(prime))
    print(len(inter))