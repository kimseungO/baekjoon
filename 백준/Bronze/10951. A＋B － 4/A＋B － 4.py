import sys
input= sys.stdin.readline

sum=[]
try:
    while True:
        a, b= map(int,input().split())
        sum.append(a+b)
except:
    for i in range(len(sum)):
        print(sum[i])