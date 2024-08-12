from collections import deque
n = int(input())

card = deque([x for x in range(n, 0, -1)])

while len(card) != 1:
    card.pop()
    card.insert(0, card.pop())

print(card[0])