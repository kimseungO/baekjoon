n = int(input())
num=[]
susik = list(input())

for i in range(n):
    num.append(int(input()))

stack=[]

for i in range(len(susik)):
    if susik[i].isalpha():
        stack.append(num[ord(susik[i])-ord('A')]) # 이 부분을 몰랐다..
    else:
        b=stack.pop()
        a=stack.pop()
        if susik[i] =='+':
            stack.append(a+b)
        elif susik[i] =='-':
            stack.append(a-b)
        elif susik[i] =='*':
            stack.append(a*b)
        elif susik[i] =='/':
            stack.append(a/b)
print('%.2f' %stack[0])