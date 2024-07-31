T = int(input())

rst = ''
for i in range(T):
    k = int(input())
    n = int(input())
    base = [[x for x in range(1, n+1)]] # 호 수
    for i in range(k):
        base.append([1 for x in range(n)]) # 층 x 호 배열
    for i in range(k):
        for j in range(n-1):
            base[i+1][j+1] = base[i+1][j] + base[i][j+1]

    print(base[k][n-1])
