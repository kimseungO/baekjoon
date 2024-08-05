n = int(input())

cnt=0
series=0
while 1:
    cnt +=1
    if str(666) in str(cnt):
        series +=1
        if series ==n:
            print(cnt)
            break