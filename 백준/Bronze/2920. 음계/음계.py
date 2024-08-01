n = list(map(int, input().split()))

sorted_n = sorted(n)
is_sorted = sorted_n == n
is_reversed = list(reversed(sorted_n)) == n
if is_sorted:
    print('ascending')

elif is_reversed:
    print('descending')

else:
    print('mixed')
