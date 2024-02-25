num=int(input())
cnt=0
for i in range(num):
    word=input()
    wrong=0
    for j in range(1, len(word)):
        if word[j] in word[:j]:
            if not word[j]==word[j-1]:
                wrong+=1
    if wrong ==0:
        cnt+=1
print(cnt)