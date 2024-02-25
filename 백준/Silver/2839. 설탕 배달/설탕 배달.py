sugar=int(input())

bag=0
while sugar>=0:
    if sugar%5 ==0: #설탕이 5로 나눠지는 경우
        bag+= (sugar//5) #그 몫 정도의 값을 가방에 넣는다
        print(bag)
        break
    sugar -=3 # 설탕이 5로 나눠지지 않는 경우 3을 빼고
    bag +=1 #가방에 1을 추가한다.
else: #sugar<0 #3과 5로 나누어 떨어지지 않는 경우 설탕이 음수가 된다.
    print(-1)
    
