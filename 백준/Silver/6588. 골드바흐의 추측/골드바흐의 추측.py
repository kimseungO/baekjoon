import sys

sosu = [1] * (1000000 + 1)
sosu[0] = 0
sosu[1] = 0

for i in range(2, 1001):
    if sosu[i]:
        for j in range(i * i, 1000001, i): # i의 배수를 지워 나감
            sosu[j] = 0
num=1
while num !=0:
    num = int(sys.stdin.readline())
    for i in range(2, num):
        if sosu[i] and sosu[num - i]:
            print("%d = %d + %d"%(num, i, num-i) )
            break