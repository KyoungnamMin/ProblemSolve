def main():
    N, M = map(int, input().split())
    array = [list(map(int, input())) for _ in range(N)]

    def dfs(x, y):
        if 0 <= x < N and 0 <= y < M:
            if array[x][y] == 0:
                array[x][y] = 1
                dfs(x - 1, y)
                dfs(x + 1, y)
                dfs(x, y - 1)
                dfs(x, y + 1)
                return True
        return False

    result = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                result += 1

    print(result)


main()
