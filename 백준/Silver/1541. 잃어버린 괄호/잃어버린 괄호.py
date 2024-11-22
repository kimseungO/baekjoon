n = input()
m = n.split('-')

for i in range(len(m)):
    m[i] = m[i].split('+')
    for j in range(len(m[i])):
        m[i][j] = int(m[i][j])
    m[i] = sum(m[i])
ans = m[0]
for i in range(1, len(m)):
    ans -= m[i]
print(ans)