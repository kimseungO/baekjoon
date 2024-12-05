from collections import deque

n, m = map(int, input().split())

def bfs(num):
    q = deque([])
    q.append(num)
    while q:
        num = q.popleft()
        for i in graph[num]:
            if visit[i] == -1:
                continue
            else:
                q.append(i)
                visit[i] = -1

graph = [[] for x in range(n+1)]
visit = [0]*(n+1)
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, n+1):
    if visit[i] == 0:
        bfs(i)
        cnt+=1
print(cnt)