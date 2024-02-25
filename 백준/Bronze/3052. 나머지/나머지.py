import sys
input= sys.stdin.readline

num=[]
for i in range(10):
    a=int(input())
    num.append(a)
for i in range(10):
    num[i]=num[i]%42
print(len(set(num)))