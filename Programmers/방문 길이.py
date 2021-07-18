def isBound(x, y):
    return True if -5<=x<=5 and -5<=y<=5 else False


def solution(dirs):
    answer = 0
    befX, befY = 0, 0
    nowX, nowY = 0, 0
    path = [[0,0,0,0]]
    
    for step in dirs:
        if step == 'U' and isBound(nowX, nowY+1):
            befX, befY = nowX, nowY
            nowY += 1
            if [befX, nowX, befY, nowY] not in path:
                path.append([befX, nowX, befY, nowY])
                path.append([nowX, befX, nowY, befY])
                answer += 1
                
        elif step == 'D' and isBound(nowX, nowY-1):
            befX, befY = nowX, nowY
            nowY -= 1
            if [befX, nowX, befY, nowY] not in path:
                path.append([befX, nowX, befY, nowY])
                path.append([nowX, befX, nowY, befY])
                answer += 1
                
        elif step == 'L' and isBound(nowX-1, nowY):
            befX, befY = nowX, nowY
            nowX -= 1
            if [befX, nowX, befY, nowY] not in path:
                path.append([befX, nowX, befY, nowY])
                path.append([nowX, befX, nowY, befY])
                answer += 1
                
        elif step == 'R' and isBound(nowX+1, nowY):
            befX, befY = nowX, nowY
            nowX += 1
            if [befX, nowX, befY, nowY] not in path:
                path.append([befX, nowX, befY, nowY])
                path.append([nowX, befX, nowY, befY])
                answer += 1
    
    return answer