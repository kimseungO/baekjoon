from collections import deque
num = int(input())

for i in range(num):
    n, m = map(int,input().split())
    paper=deque()
    imp = list(map(int,input().split()))
    for j in range(n):
        paper.append((j,imp[j]))

    target = paper[m]
    cnt=0
    while True:
        if paper[0][1] == max(imp):
            ans = paper.popleft()
            imp.remove(max(imp))
            cnt+=1
            if target == ans:
                print(cnt)
                break
        else:
            paper.append(paper.popleft())
