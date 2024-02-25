num=list(range(int(input())+1))

for i in range(len(num)):
    num[i]=[int(x) for x in str(i)]
del num[0]

count=0
for i in num:
    if len(i)<3:
        count+=1
    elif i[1]-i[0]==i[2]-i[1]:
        count+=1
print(count)