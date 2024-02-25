import sys
input= sys.stdin.readline

a=int(input())
b=int(input())
c=int(input())
abc=a*b*c
num=[int(x) for x in str(abc)]
for i in range(10):
    print(num.count(i))