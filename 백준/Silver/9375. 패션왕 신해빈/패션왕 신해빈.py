from collections import Counter

test_case = int(input())

for i in range(test_case):
    n = int(input())
    wardrobe = {}
    for i in range(n):
        cloths, types = input().split()
        wardrobe[cloths] = types
    value_cnt = Counter(wardrobe.values())

    cnt = 1
    for i in list(value_cnt.values()):
        cnt *= (i+1)
    print(cnt-1)