N=int(input())
sosu=list(map(int,input().split()))

cnt=0
for i in sosu:
    a=i
    while i>1:
        a -=1
        if a==1: #소수일 때
            cnt+=1 #카운트
            break
        if i%a ==0: # 소수가 아닐때
            break #카운트 하지 않고 브레이크
print(cnt)