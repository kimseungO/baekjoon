def d(n):
    a=[int(x) for x in str(n)]
    return(sum(a)+n)

count=[]
for n in range(10000):
    c=d(n)
    count.append(c)
num=list(range(10000))

for i in range(10000):
    if num[i] not in count:
        print(num[i])