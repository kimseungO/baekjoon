miss=list(input().upper())
cnt=[]
newmiss=[]
for i in miss:
    if i not in newmiss:
        newmiss.append(i)
for i in newmiss:
    counta=0
    for j in miss:
        if i==j:
            counta+=1
    cnt.append(counta)
ma=max(cnt)
newcnt=[]
for i in cnt:
    newcnt.append(i)
del cnt[cnt.index(max(cnt))]
if ma in cnt:
    print('?')
else:
    print(newmiss[newcnt.index(max(newcnt))])