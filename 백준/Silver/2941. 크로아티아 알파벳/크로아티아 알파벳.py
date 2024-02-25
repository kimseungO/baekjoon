word=input()
for i in range(len(word)):
    if 'c=' in word:
        word=word.replace("c=","*")
    elif 'c-' in word:
        word=word.replace('c-','*')
    elif 'dz=' in word:
        word=word.replace('dz=','*')
    elif 'd-' in word:
        word=word.replace('d-','*')
    elif 'lj' in word:
        word=word.replace('lj','*')
    elif 'nj' in word:
        word=word.replace('nj','*')
    elif 's=' in word:
        word=word.replace('s=','*')
    elif 'z=' in word:
        word=word.replace('z=','*')
print(len(word))