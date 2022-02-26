def find_rect_size(x, y):
    maximum = 100
    for i in range(100):
        if x + i > 100:
            break
        for j in range(100):
            if y + j > 100:
                break
            maximum = max(maximum, calc_area(x, y, x + i, y + j))
    return maximum


def calc_area(x, y, h, w):
    count = 0
    for i in range(x, h + 1):
        for j in range(y, w + 1):
            if arr[i][j] == 0:
                return 0
            else:
                count += 1
    return count


T = int(input())
arr = [[0] * 101 for _ in range(101)]
for _ in range(T):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            arr[i][j] = 1

maximum = 100
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            maximum = max(maximum, find_rect_size(i, j))

print(maximum)
