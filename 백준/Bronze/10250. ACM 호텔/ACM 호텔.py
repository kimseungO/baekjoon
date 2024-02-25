T=int(input())
T_list=[]
for i in range(T):  #값 입력 받음
    H,W,N=map(int,input().split())
    W=list(range(1,W+1))
    hotel=[]
    new_hotel=[]
    for i in W:  #층을 문자형으로 hotel리스트에 저장
        a=str(i)
        if len(a)<2:
            hotel.append(str(0)+a)
            continue
        hotel.append(a)
    for i in hotel:  #hotel리스트를 new_hotel로 호수 채워주기
        for j in range(1,H+1):
            a=str(j)+str(i)
            new_hotel.append(a)
    new_hotel=[int(x) for x in new_hotel]
    T_list.append(new_hotel[N-1])
for i in range(T):
    print(T_list[i])