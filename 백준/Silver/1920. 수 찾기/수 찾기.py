
n = int(input())
answer = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))

# 1. 정렬
answer.sort()


for i in num:
    start = 0
    end = n-1
    isExist = False

    while start <= end:
        mid = (start+end)//2
        if i == answer[mid]:
            isExist = True
            print(1)
            break
        elif i < answer[mid]:
            end = mid -1
        else: 
            start = mid +1
        
    if not isExist:
        print(0)