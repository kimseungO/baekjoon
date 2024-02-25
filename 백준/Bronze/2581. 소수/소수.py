import sys
input=sys.stdin.readline
M=int(input())
N=int(input())
sosu=range(M,N+1)

cnt=[]
for i in sosu:
    error=0
    if i>1:
        for a in range(2,i):
            if i%a ==0: #소수 아닐 때
                error+=1 #에러 올리기
        if error==0: #소수
            cnt.append(i) #카운트
if len(cnt)!=0:
    print(sum(cnt))
    print(cnt[0])
else:
    print(-1)