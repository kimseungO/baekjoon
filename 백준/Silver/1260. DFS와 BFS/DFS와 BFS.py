import sys
from collections import deque
input = sys.stdin.readline

def dfs(num):
    for i in arr[num]:
        if i not in res:
            res.append(i)
            dfs(i)
def bfs(num):
    q = deque()
    q.append(num) 
    while q:
        num = q.popleft()
        for i in arr[num]:
            if i not in res and i != -1:
                res.append(i)
                arr[num][arr[num].index(i)] = -1
                q.append(i)

n, m, v = map(int,input().split())
arr =[[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in arr:
    i.sort()       

res = [v]
dfs(v)
print(*res)
res = [v]
bfs(v)
print(*res)