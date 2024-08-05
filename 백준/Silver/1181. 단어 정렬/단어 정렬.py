n = int(input())

wlist=[]
for i in range(n):
    wlist.append(input())

set_=list(set(wlist))
set_.sort()
sorted_=sorted(set_, key=len)
for i in range(len(sorted_)):
    print(sorted_[i])