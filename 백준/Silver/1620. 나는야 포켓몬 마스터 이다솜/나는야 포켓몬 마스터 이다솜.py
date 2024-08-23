n, m = map(int, input().split())
dic={}
rev_dic={}
quiz=[]
for i in range(1, n+1):
    monster = input()
    dic[i] = monster
    rev_dic[monster] = i

for i in range(m):
    quiz=input()
    if quiz.isdigit():
        print(dic.get(int(quiz)))
    else:
        print(rev_dic.get(quiz))