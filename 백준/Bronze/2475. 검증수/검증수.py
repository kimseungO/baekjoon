num = list(map(int, input().split()))
res=0
for i in range(len(num)):
    res+=num[i]**2
print(res%10)