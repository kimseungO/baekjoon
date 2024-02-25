
# 다섯 줄 입력받기
toy =[]
for i in range(5):
    toy.append(list(x for x in input()))

# 출력되는 열 값 정하기
max = 0
for i in toy:
    if len(i)>max:
        max=len(i)
        
# 세로 출력
output=[]
for i in range(max):
    for j in range(5):
        try:
            output.append(toy[j][i])
        except:
            pass
        
for i in output:
    print(i, end='')