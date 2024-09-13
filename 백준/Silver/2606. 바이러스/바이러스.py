def dfs(c):
    global ans

    ans+=1
    v[c]=1
    
    for i in arr[c]:
        if v[i] == 0:
            dfs(i)

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)
    # [[], [2,5], [1,3], [2], [7], [2, 6], [5], [4]]

ans=0
v=[0] *(n+1)
dfs(1)
print(ans-1)