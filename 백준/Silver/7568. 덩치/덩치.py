n = int(input())

sizeli =[]
for i in range(n):
    size = list(map(int, input().split()))
    sizeli.append(size)

hrank=[]
for i in range(n):
    hcnt=1
    for j in range(n):
        if sizeli[i][0] < sizeli[j][0]:
            if sizeli[i][1] < sizeli[j][1]:
                hcnt +=1
    hrank.append(hcnt)

print(*hrank)
