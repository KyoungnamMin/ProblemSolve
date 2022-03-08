# 가로세로 1
dx1 = [-1, 1, 0, 0]
dy1 = [0, 0, -1, 1]
# 가로세로 2
dx2 = [-2, 2, 0, 0]
dy2 = [0, 0, -2, 2]
# 대각선
dx3 = [-1, -1, 1, 1]
dy3 = [-1, 1, -1, 1]


def oob(x, y):
    return x < 0 or x > 4 or y < 0 or y > 4


def check(place):
    # 하나의 대기실 구조
    for i in range(5):
        for j in range(5):
            if place[i][j] != "P":
                continue
            # 가로세로 거리 1 - 사람 있으면 X
            for d in range(4):
                nx = i + dx1[d]
                ny = j + dy1[d]
                if oob(nx, ny):
                    continue
                if place[nx][ny] == "P":
                    return 0

            # 가로세로 거리 2 - 사람 있으면 - 그 사이에 파티션 없으면 X
            for d in range(4):
                nx = i + dx2[d]
                ny = j + dy2[d]
                if oob(nx, ny):
                    continue
                if place[nx][ny] == "P":
                    if place[i + dx1[d]][j + dy1[d]] != "X":
                        return 0
            # 대각선
            for d in range(4):
                nx = i + dx3[d]
                ny = j + dy3[d]
                if oob(nx, ny):
                    continue
                if place[nx][ny] == "P":
                    if place[i][ny] != "X" or place[nx][j] != "X":
                        return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))

    return answer
