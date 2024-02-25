a,b,c=map(int,input().split())
if c>b:
    son=int(a/(c-b))
    print(son+1)
else:
    print(-1)