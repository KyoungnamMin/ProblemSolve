from collections import deque


def solution(priorities, location):
    answer = 0
    dq = deque((v, i) for i, v in enumerate(priorities))

    while dq:
        now = dq.popleft()
        if dq and max(dq)[0] > now[0]:
            dq.append(now)
        else:
            answer += 1
            if now[1] == location:
                break
            
    return answer