num=int(input())
cycle6=1
i=0
while True:
    cycle6=6*i+cycle6
    i+=1
    if cycle6>=num:
        break
print(i)