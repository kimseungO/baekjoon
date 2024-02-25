import sys
input= sys.stdin.readline

num=int(input())

a=[int(x) for x in str(num)]
count=0
while True:
    if len(a) ==1 :
        a.insert(0, 0)
    a.append(a[0]+a[1])
    del a[0]
    if a[1]>=10:
        a[1]=[int(x) for x in str(a[1])]
        del a[1][0]
        a[1]=a[1][0]
    a.append(str(a[0])+str(a[1]))
    del a[0]
    del a[0]
    count+=1
    a[0]=int(a[0])
    if num==a[0]:
        break
    a=[int(x) for x in str(a[0])]
print(count)