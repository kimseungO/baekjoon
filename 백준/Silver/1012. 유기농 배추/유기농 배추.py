
from collections import deque
t = int(input())

def bfs(x, y):
    q = deque()
    q.append([x, y])
    graph[y][x] == 0

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0<= ax <m and 0<= ay <n:
                if graph[ay][ax] == 1:
                    q.append([ax, ay])
                    graph[ay][ax] = 0

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0 for x in range(m)] for x in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0
    for a in range(m):
        for b in range(n):
            if graph[b][a] == 1:
                bfs(a, b)
                cnt += 1
    print(cnt)
