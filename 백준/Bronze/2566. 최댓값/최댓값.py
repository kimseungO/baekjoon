num = []

# 9x9 리스트 만들기
for i in range(9):
    num.append(list(map(int,input().split())))


# 최댓값, 최댓값 위치 찾기
max = 0
low=0
column=0
for i in num:
    for j in i:
        if j > max:
            max = j
            low = num.index(i)
            column = i.index(j)

print(max)
print(low+1, column+1)