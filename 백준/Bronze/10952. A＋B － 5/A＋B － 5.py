import sys
input= sys.stdin.readline

sum=[]
while True:
    a, b= map(int,input().split())
    if a==0 and b==0:
        break
    sum.append(a+b)
for i in range(len(sum)):
    print(sum[i])