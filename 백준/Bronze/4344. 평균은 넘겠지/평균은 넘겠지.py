C=int(input())

N=[]
for i in range(C):
    N.append(list(map(int,input().split())))

for i in N:
    count=0
    a=i[0]
    del i[0]
    for j in i:
        if j>(sum(i)/a):
            count+=1
        b=(count/len(i))*100
    print("%0.3f%%"%b)