N, K = map(int, input().split())
count = 0

while 1:
    if N == 1:
        break

    if N // K != 0 and N % K == 0:
        N = N // K
    else:
        N -= 1

    count += 1

print(count)
