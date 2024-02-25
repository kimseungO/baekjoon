num=int(input())
a=[]
for i in range(num):
    a.append(input())

for i in range(num):
    a[i]=[x for x in str(a[i])]
count=0
upcount=0
for i in a:
    count=0
    upcount=0
    for j in range(len(i)):
        if i[j]=='O':
            count+=1
            upcount+=count
        elif i[j]=='X':
            count=0
    print(upcount)

