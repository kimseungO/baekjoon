import sys
num = int(sys.stdin.readline())

stack = []

for i in range(num):
    X = sys.stdin.readline().split()

    if X[0] == 'push':
        stack.append(X[1])

    elif X[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif X[0] == 'size':
        print(len(stack))

    elif X[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif X[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
