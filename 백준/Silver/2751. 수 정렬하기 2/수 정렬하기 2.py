import sys
input = sys.stdin.readline
n = int(input())

nlist=[]
for i in range(n):
    num = int(input())
    nlist.append(num)

def merge_sort(nlist):
    if len(nlist) < 2:
        return nlist
    
    half = len(nlist)//2

    low = merge_sort(nlist[:half])
    high = merge_sort(nlist[half:])
    merged_=[]
    l = h = 0
    while l < len(low) and h < len(high):
        if low[l] < high[h]:
            merged_.append(low[l])
            l+=1
        else:
            merged_.append(high[h])
            h+=1

    merged_ += low[l:]
    merged_ += high[h:]
    return merged_

merged_ =merge_sort(nlist)

for i in range(n):
    print(merged_[i])