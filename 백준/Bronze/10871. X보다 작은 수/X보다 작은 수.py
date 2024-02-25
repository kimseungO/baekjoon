import sys
input= sys.stdin.readline
a, b= map(int,input().split())

#list=[a]
list1=input().split()
list2=[]
for i in range(a):
    if int(list1[i])<b:
        list2.append(list1[i])
print(*list2)