n, k = map(int, input().split())

que = [x for x in range(1, n+1)]
result = []
i = 0
while que:
    i = (i + k-1) % len(que)
    result.append(str(que.pop(i)))
print("<",', '.join(result),">", sep='')