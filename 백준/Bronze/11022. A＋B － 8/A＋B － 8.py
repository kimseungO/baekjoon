import sys
input= sys.stdin.readline
a= int(input())

sum=[]
numone=[]
numtwo=[]
for i in range(a):
    num1, num2= map(int, input().split())
    numone.append(num1)
    numtwo.append(num2)
    sum.append(num1+num2)
for i in range(a):
    print("Case #{0}: {1} + {2} =".format(i+1,numone[i],numtwo[i]), sum[i])
    