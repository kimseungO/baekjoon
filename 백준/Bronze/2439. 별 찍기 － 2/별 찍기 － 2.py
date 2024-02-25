import sys
input= sys.stdin.readline
a= int(input())

sum=[]
b=0
for i in range(a):
    b=b+1
    sum.append('*'*b)
for i in range(a):
    print(sum[i].rjust(a))