n, k = map(int, input().split())

coin=[]
for i in range(n):
    coin.append(int(input()))

cnt=0
for i in range(n):
    if k//coin[-1]:
        cnt += k//coin[-1]
        k = k%coin[-1]
    coin.pop()

print(cnt)