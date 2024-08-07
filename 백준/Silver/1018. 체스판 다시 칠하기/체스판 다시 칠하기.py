n, m = map(int, input().split())

board=[]
for i in range(n):
    line = list(x for x in input())
    board.append(line)

ans1=[
    ['WBWBWBWB'],
    ['BWBWBWBW'],
    ['WBWBWBWB'], 
    ['BWBWBWBW'], 
    ['WBWBWBWB'], 
    ['BWBWBWBW'], 
    ['WBWBWBWB'], 
    ['BWBWBWBW']]
ans2=[
    ['BWBWBWBW'],
    ['WBWBWBWB'], 
    ['BWBWBWBW'], 
    ['WBWBWBWB'], 
    ['BWBWBWBW'], 
    ['WBWBWBWB'], 
    ['BWBWBWBW'],
    ['WBWBWBWB']]
for i in range(8):
    ans1[i] = list(ans1[i][0])
    ans2[i] = list(ans2[i][0])

cntlst=[]
cnt1=0
cnt2=0
for row in range(n-7):
    for col in range(m-7):
        ansi =0
        for i in range(row, row+8):
            ansj =0
            for j in range(col, col+8):
                if board[i][j] != ans1[ansi][ansj]:
                    cnt1+=1
                if board[i][j] != ans2[ansi][ansj]:
                    cnt2+=1
                ansj +=1
            ansi +=1
        cntlst.append(cnt1)
        cntlst.append(cnt2)
        cnt1 = 0
        cnt2 = 0

print(min(cntlst))