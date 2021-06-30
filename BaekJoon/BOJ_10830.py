def matrix_solve(num):
    global N, A
    if num == 1:
        for i in range(N):
            for j in range(N):
                A[i][j] %= 1000
        return A
    elif num % 2 == 1:
        tmp = [[0] * N for _ in range(N)]
        C = matrix_solve(num - 1)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j] += C[i][k] * A[k][j]
                tmp[i][j] %= 1000
        return tmp
    else:
        tmp = [[0] * N for _ in range(N)]
        C = matrix_solve(num // 2)
        for i in range(N):
            for j in range(N):
                for k in range(N):
                    tmp[i][j] += C[i][k] * C[k][j]
                tmp[i][j] %= 1000
        return tmp

N, B = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
res = matrix_solve(B)

# 출력
for i in range(N):
    for j in range(N):
        print(res[i][j], end=" ")
    print()