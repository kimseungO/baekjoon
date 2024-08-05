num = int(input())
tsize = list(map(int,input().split()))
t, p = map(int,input().split())

tcnt=0
for i in tsize:
    tcnt += i//t
    if i%t:
        tcnt+=1

print(tcnt)
print(num//p, num%p)
