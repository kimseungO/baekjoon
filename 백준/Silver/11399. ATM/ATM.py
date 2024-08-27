n = int(input())
line = list(map(int, input().split()))
line.sort()

cnt=0
res=0
for i in range(n):
    cnt += line[i]
    res += cnt
print(res)