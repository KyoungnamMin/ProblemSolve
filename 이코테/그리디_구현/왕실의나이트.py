from operator import countOf


knight = input()

x = int(knight[1]) - 1
y = ord(knight[0]) - 97

dx = [1, -1, 1, -1, 2, 2, -2, -2]
dy = [2, 2, -2, -2, 1, -1, 1, -1]

count = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < 8 and 0 <= ny < 8:
        count += 1

print(count)
