import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
ngf = [-1]*n
stack = []
count = [0]*1000001

for i in li:
    count[i] = count[i] + 1

stack.append(0)
for i in range(n):
    while stack and count[li[stack[-1]]] < count[li[i]]:
        ngf[stack.pop()] = li[i]
    stack.append(i)

print(*ngf)