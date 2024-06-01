import sys
import math
n = int(sys.stdin.readline())

for i in range(n):
    m = list(map(int, sys.stdin.readline().split()))
    cnt=0
    for j in range(1, len(m)):
        for k in range(j+1, len(m)):
            cnt += math.gcd(m[j], m[k])
    print(cnt)