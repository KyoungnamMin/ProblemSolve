import sys

input = sys.stdin.readline

N, K = map(int, input().split())

div = 1
answer = []
while div <= N:
    if N % div == 0:
        answer.append(div)
    div += 1

if len(answer) < K:
    print(0)
else:
    print(answer[K - 1])
