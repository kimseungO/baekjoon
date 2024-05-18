sentence = list(input())
status = False

stack=[]
result=[]
for i in sentence:
    if i =='<' or status == True:
        if stack:
            stack = stack[::-1]
            result = result + stack
            stack =[]
        status = True
        result.append(i)
        if i =='>':
            status = False
    else:
        if i == ' ':
            stack = stack[::-1]
            stack.append(' ')
            result = result + stack
            stack=[]
        else:
            stack.append(i)
print(''.join(result+stack[::-1]))