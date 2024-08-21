import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lan=[]
for i in range(k):
    lan.append(int(input()))

start = 0
end = max(lan)
pivot = end
piv_lst=[]
isExist=False
while start < pivot <= end:
    cnt=0
    for i in lan:
        cnt += i//pivot
    if cnt >= n:
        start = pivot
        piv_lst.append(pivot)
    elif cnt < n :
        end = pivot
    pivot = (start+end)//2
        
    if pivot == 0:
        print(0)
        isExist=True
        break
if isExist == False:
    print(max(piv_lst))