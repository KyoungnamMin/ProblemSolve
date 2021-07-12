import sys
input = sys.stdin.readline

n, k = map(int, input().split())

answer = 0
important = 0
LT=[]

for _ in range(n):
    L, T = map(int, input().split())
    if T == 1: important += 1
    LT.append((L, T))

LT.sort()
if important - k <= 0:
    for i in LT:
        answer += i[0]
else:
    delete_count = important - k
    for val in LT:
        if delete_count > 0:
            if val[1] == 1:
                delete_count -= 1
                answer -= val[0]
            else:
                answer += val[0]
        else:
            answer += val[0]

print(answer)