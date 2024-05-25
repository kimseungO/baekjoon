word = input()

stack =[]
rst =''
for i in range(len(word)):
    stack.append(word[i:])
stack.sort()
for i in range(len(word)):
    print(stack[i])
