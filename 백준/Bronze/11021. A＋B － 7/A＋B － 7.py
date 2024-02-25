import sys
input= sys.stdin.readline
a= int(input())

sum=[]
for i in range(a):
    num1, num2= map(int, input().split())
    sum.append(num1+num2)
for i in range(a):
    print("Case #{0}:".format(i+1), sum[i])