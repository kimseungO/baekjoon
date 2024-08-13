while 1:
    stack=[]
    isEnd=False
    word = input()
    if word == '.':
        break
    word = [x for x in word]

    for i in range(len(word)):
        if word[i] == '(' or word[i] == '[':
            stack.append(word[i])
        elif word[i] == ')':
            if stack:
                if stack[-1] != '(':
                    print('no')
                    isEnd=True
                    break
                stack.pop()
            else:
                print('no')
                isEnd=True
                break
        elif word[i] == ']':
            if stack:
                if stack[-1] != '[':
                    print('no')
                    isEnd=True
                    break
                stack.pop()
            else:
                print('no')
                isEnd=True
                break
            
    if isEnd ==False:
        if len(stack):
            print('no')
        else:
            print('yes')