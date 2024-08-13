n = int(input())

xylst=[]
for i in range(n):
    x, y = map(int, input().split())
    xylst.append((x, y))

xylst.sort(key= lambda x:x[1])
xylst.sort(key= lambda x:x[0])

for i in range(n):
    print(*xylst[i])