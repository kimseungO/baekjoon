import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
nge = [-1]*n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and li[stack[-1]] < li[i]:
        nge[stack.pop()] = li[i]
    stack.append(i)

print(*nge)