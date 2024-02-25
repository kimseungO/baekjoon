N, M= map(int,input().split())

alist = [] # N*M 행렬
blist = []
sumlist=[]

for j in range(N): # N*M 행렬 생성
    c = list(map(int,input().split()))
    alist.append(c)

for j in range(N):
    c = list(map(int,input().split()))
    blist.append(c)

for i in range(N): # N*M 행렬 더한 후 출력
    for j in range(M):
        sumlist.append(alist[i][j] + blist[i][j])
    print(*sumlist)
    sumlist=[]
