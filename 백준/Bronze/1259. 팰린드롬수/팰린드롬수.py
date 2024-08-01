n = 1
while True:
    n = str(input())
    lengs = len(n)
    leng = lengs//2

    half_n = n[:leng]
    half_n = half_n[::-1]
    if lengs%2 ==1:
        leng+=1
    if n =='0':
        break
    elif half_n == n[leng:]:
        print('yes')
    else:
        print('no')