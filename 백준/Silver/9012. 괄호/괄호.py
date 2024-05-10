num = int(input())

for i in range(num):
    vps = input()
    vps = list(vps)
    stack=[]
    for j in vps:
        if len(stack) == 0:
            if j == ')':
                stack.append(j)
                break
            elif j =='(':
                stack.append(j)
        else:
            if j ==')':
                stack.pop()
            elif j =='(':
                stack.append(j)
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")