import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
prefix = [0]
for i in range(n):
    prefix.append(prefix[i]+num[i])
    
for _ in range(m):
    i, j = map(int, input().split())
    res = prefix[j]-prefix[i-1]
    print(res)