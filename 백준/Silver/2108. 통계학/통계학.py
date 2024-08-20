import sys
input = sys.stdin.readline

n = int(input())

num=[]
for i in range(n):
    num.append(int(input()))

# 산술평균
mean=round(sum(num)/n)

# 중앙값
sorted_num=sorted(num)
median=sorted_num[n//2]

# 최빈값
dic={}
for i in num:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] =1
mode=max(dic, key= dic.get)
sorted_dic = sorted(dic.items())
all_value=dic.values()
max_value=max(all_value)
cnt=0
for i in sorted_dic: # i = 키 값
    if max_value == i[1]:
        cnt+=1
        if cnt ==2:
            mode=i[0]
            break

# 범위
ranger=max(num)-min(num)

print(mean)
print(median)
print(mode)
print(ranger)