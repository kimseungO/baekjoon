a= int(input())
b= int(input())
if 0<a:
    if 0<b:
        print('1')
    elif 0>b:
        print('4')
elif 0>a:
    if 0<b:
        print('2')
    elif 0>b:
        print('3')
