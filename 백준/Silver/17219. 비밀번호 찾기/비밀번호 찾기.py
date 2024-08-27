import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic={}
for i in range(n):
    site, pw = input().strip().split()
    dic[site] = pw
for i in range(m):
    find_site = input().strip()
    print(dic[find_site])