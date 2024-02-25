a, b=map(int,input().split())
a=[x for x in str(a)]
a.reverse()
rev_a=''.join(a)
rev_a=int(rev_a)
b=[x for x in str(b)]
b.reverse()
rev_b=''.join(b)
rev_b=int(rev_b)
if rev_a>rev_b:
    print(rev_a)
else:
    print(rev_b)