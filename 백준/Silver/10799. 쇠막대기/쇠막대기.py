word = list(input())

stack=[]
cnt=0
for i in range(len(word)):
    if word[i] == '(':
        stack.append(word[i])
    else:
        if word[i-1] == '(':
            stack.pop()
            cnt = cnt + len(stack)
        else:
            stack.pop()
            cnt = cnt + 1
print(cnt)