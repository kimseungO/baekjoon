n = int(input())

for i in range(1, n+1):
    k = str(i) # '198'
    nlist = [x for x in k] # ['1', '9', '8']
    res=i
    for j in nlist:
        res += int(j) # 1 + 9 + 8 =18
    if res == n:
        print(i)
        break
    if i == n:
        print(0)
