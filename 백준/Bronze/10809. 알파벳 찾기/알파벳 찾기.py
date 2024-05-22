word = input()

stk=[-1]*26
for i in range(26):
    if chr(i+97) in word:
        stk[i] = word.index(chr(i+97))
print(*stk)