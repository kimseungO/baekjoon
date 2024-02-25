baekjoon=list(map(str,input()))
atoz='abcdefghijklmnopqrstuvwxyz'
atoz=list(map(str,atoz))
solut=[]
for i in atoz:
    if i in baekjoon:
        solut.append(baekjoon.index(i))
    else:
        solut.append(-1)
print(*solut)