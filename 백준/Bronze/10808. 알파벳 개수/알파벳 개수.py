word = input()

stk=[0]*26
for i in word:
    a= ord(i)-97
    stk[a] = stk[a] + 1

print(*stk)