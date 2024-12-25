T = int(input())

for i in range(T):
    H,W,N = map(int,input().split())
    X = N % H
    Y = N // H
    if X == 0:
        print(H * 100 + Y)
    else:
        print((X*100)+(Y+1))