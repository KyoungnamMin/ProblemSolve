def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    N = len(A)
    for i in range(N):
        answer += A[i] * B[N - i - 1]

    return answer


"""
Test1
[1,4,2]
[5,4,4]
29
"""
A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A, B))
