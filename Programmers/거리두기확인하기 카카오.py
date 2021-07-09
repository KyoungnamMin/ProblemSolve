dx1 = [-1, 1, 0, 0]
dy1 = [0, 0, -1, 1]

dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]

dx3 = [-2, 2, 0, 0]
dy3 = [0, 0, -2, 2]


def oob(x, y):
    return x<0 or x>4 or y<0 or y>4
    

def check(place):
    for i in range(5):
        for j in range(5):
            if place[i][j] != 'P': continue
            # 가로세로 거리 1
            for d in range(4):
                nx = i + dx1[d]
                ny = j + dy1[d]
                if oob(nx, ny): continue
                if place[nx][ny] == 'P':
                    return False
            # 대각선
            for d in range(4):
                nx = i + dx2[d]
                ny = j + dy2[d]
                if oob(nx, ny): continue
                if place[nx][ny] == 'P':
                    if place[i][ny] != 'X' or place[nx][j] != 'X':
                        return False
            
            # 가로세로 거리 2
            for d in range(4):
                nx = i + dx3[d]
                ny = j + dy3[d]
                if oob(nx, ny): continue
                if place[nx][ny]=='P':
                    if place[i+dx1[d]][j+dy1[d]] != 'X':
                        return False
    return True


def solution(places):
    answer = []
    for place in places:
        answer.append(int(check(place)))

    return answer