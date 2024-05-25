word = input()
rot13=''

for i in word:
    if 64 < ord(i) < 91:
        i = ord(i)+13
        if i > 90:
            i = i - 26
        i = chr(i)

    elif 96 < ord(i) < 123:
        i = ord(i)+13
        if i > 122:
            i = i - 26
        i = chr(i)
        
    rot13 += i
print(rot13)