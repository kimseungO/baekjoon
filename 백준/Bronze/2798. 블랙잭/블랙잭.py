n, m = map(int, input().split())

nlist=list(map(int, input().split()))

cnt=[]
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            hap = nlist[i] + nlist[j] + nlist[k]
            if m-hap >= 0:
                cnt.append(hap)
print(max(cnt))