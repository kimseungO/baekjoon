n = int(input())
word = list(input())
r = 31
M = 1234567891
wordnum = []

for i in range(n):
    num = (ord(word[i])-ord('a')+1) *(r**(i))
    wordnum.append(num)

print(sum(wordnum)%M)