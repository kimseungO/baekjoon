
for test_case in range(1, 10 + 1):
    dump_num = int(input())
    box_hi = list(map(int, input().split()))

    for i in range(dump_num):
        if max(box_hi) - min(box_hi) >= 2:
            box_hi[box_hi.index(max(box_hi))] -= 1
            box_hi[box_hi.index(min(box_hi))] += 1
        else:
            break
    ans = max(box_hi) - min(box_hi)
    print(f"#{test_case} {ans}")