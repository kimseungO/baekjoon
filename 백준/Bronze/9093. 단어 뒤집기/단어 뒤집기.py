num = int(input())

for i in range(num):
    word = input().split()
    reversed_word=[]
    
    # 원소 갯수만큼 반복
    for j in range(len(word)):
        re_word = list(word[j])
        re_word.reverse()
        reversed_word.append(''.join(re_word))
    print(' '.join(reversed_word))