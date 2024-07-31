N = int(input())

numlst=[]
for i in range(N):
    num = int(input())
    numlst.append(num)
for j in range(N):
    for i in range(N-1):
        if numlst[i] > numlst[i+1]:
            numlst[i], numlst[i+1] = numlst[i+1], numlst[i]

for i in numlst:
    print(i)