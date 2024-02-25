import sys
input= sys.stdin.readline

num=int(input())
a=input().split()
b=[]

for i in range(num):
    a[i]=int(a[i])
for i in range(num):
    b.append((a[i]/max(a))*100)
print(sum(b)/num)