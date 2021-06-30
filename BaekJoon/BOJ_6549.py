import sys

while True:
    height = list(map(int, sys.stdin.readline().split())) + [0]
    if height[0] == 0:
        break

    n = height[0]
    stack = [(1, height[1])]
    result = 0
    for i in range(2, n+2):
        w = i
        while stack and stack[-1][1] > height[i]:
            w, hi = stack.pop()
            result = max(result, (i - w) * hi)
        stack.append((w, height[i]))
    print(result)