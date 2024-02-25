a, b= map(int, input().split())

M = b-45
if M<0:
    M = 60+M
    a = a-1
    if a<0:
        a = 24+a
        print(a, M)
    elif a>=0:
        print(a, M)
else:
    print(a, M)
