num = int(input())
exam = [] #43687521
stack = [] 
result = []
a = True
for i in range(1, num+1): 
    n = int(input())
    exam.append(n)
i = 1
while len(exam) != 0:
    if len(stack) == 0:
        stack.append(i)
        result.append('+')
        i += 1
    if stack[-1] == exam[0]: #pop
        stack.pop()
        exam.remove(exam[0])
        result.append('-')
    elif stack[-1] > exam[0]:
        print("NO")
        a = False
        break
    else: #push
        stack.append(i)
        i += 1
        result.append('+')
if a == True:
    for i in result:
        print(i)