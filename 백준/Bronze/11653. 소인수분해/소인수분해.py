N=int(input())

soinsu=2
while N>1:
    if N%soinsu ==0:
        N =N/soinsu
        print(soinsu)
    else:
        soinsu+=1