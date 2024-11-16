n = int(input())
ans = []
for i in range(1, n+1):
    i = [x for x in str(i)]
    # print(i)
    stk = []
    if '3' in i or '6' in i or '9' in i:
        for j in i:
            if j == '3' or j == '6' or j == '9':
                stk.append('-')
    else:
        for j in i:
            stk.append(j)
    ans.append("".join(stk))
print(*ans)