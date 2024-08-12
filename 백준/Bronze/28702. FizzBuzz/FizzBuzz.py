wlst = []
for i in range(3):
    wlst.append(input())

for j in range(len(wlst)):
    if wlst[j].isdigit():
        wlst[j] = int(wlst[j])
        if j == 0:
            n=wlst[j]+3
        elif j ==1:
            n=wlst[j]+2
        elif j ==2:
            n=wlst[j]+1

if n%3 ==0 and n%5 ==0:
    print('FizzBuzz')
elif n%3 ==0:
    print('Fizz')
elif n%5 ==0:
    print('Buzz')
else:
    print(n)