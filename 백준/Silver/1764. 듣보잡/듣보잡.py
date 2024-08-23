import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst=set([])
for i in range(n):
    lst.add(input().strip())

chcklst=[]
for i in range(m):
    aa = input().strip()
    if aa in lst:
        chcklst.append(aa)
chcklst.sort()
print(len(chcklst))
for i in chcklst:
    print(i)