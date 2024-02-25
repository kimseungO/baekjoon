a, b= map(int, input().split())
c= int(input())

b= c+b
if b>=60:
    a= a+(b//60)
    b= b%60
    if a>23:
        a= a-24
        print(a, b)
    else:
        print(a, b)
else:
    print(a, b)