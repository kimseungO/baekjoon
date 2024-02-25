a= int(input())

plused=[]
for i in range(a):
    num1, num2= map(int,input().split())
    plused.append(num1+num2)
for i in range(a):
    print(plused[i])