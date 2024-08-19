import sys
from collections import deque

input=sys.stdin.readline
n = int(input())

def roundy(x):
    if x - int(x) >= 0.5:
        return int(x) +1
    else:
        return int(x)

level=[]
for i in range(n):
    level.append(int(input()))
level.sort()
level=deque(level)

trim = roundy(len(level)*0.15)
for i in range(trim):
    level.pop()
    level.popleft()

try:
    print(roundy(sum(level)/len(level)))
except ZeroDivisionError:
    print(0)