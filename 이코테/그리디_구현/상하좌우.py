def main():
    def is_inside(x, y):
        return True if (0 <= x < N and 0 <= y < N) else False

    N = int(input())
    move = list(map(str, input().split()))

    x, y = 0, 0
    for m in move:  # R L U D
        if m == "R" and is_inside(x, y + 1):
            y += 1
        if m == "L" and is_inside(x, y - 1):
            y -= 1
        if m == "U" and is_inside(x - 1, y):
            x -= 1
        if m == "D" and is_inside(x + 1, y):
            x += 1

    print(x + 1, y + 1)


main()
