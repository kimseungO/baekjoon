num=int(input())
QR=[]
for i in range(num):
    QR.append(list(input().split()))

for i in QR:
    a=int(i[0])
    del i[0]
    b=i[0]
    result=[]
    for j in b:
        result.append(a*j)
    print(''.join(result))