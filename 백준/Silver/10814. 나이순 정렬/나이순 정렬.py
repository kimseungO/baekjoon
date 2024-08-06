n = int(input())

member=[]
for i in range(n):
    age, name = input().split()
    member.append([int(age), name])
sorted_ = sorted(member, key=lambda x: x[0])
for i in range(n):
    print(*(sorted_[i]))