def solution(dartResult):
    answer = []
    before = 0
    before_idx = -1
    for i in range(len(dartResult)):
        now = dartResult[i]
        if now.isdigit() and not dartResult[i-1].isdigit():
            # 10점
            if dartResult[i+1].isdigit():
                before = 10
                before_idx += 1
            else:
                before = int(now)
                before_idx += 1
        elif now.isalpha():
            if now == 'S':
                answer.append(before**1)
            elif now == 'D':
                answer.append(before**2)
            elif now == 'T':
                answer.append(before**3)
        else:
            if now == '*':
                if before_idx == 0:
                    answer[before_idx] *= 2
                else:
                    answer[before_idx-1] *= 2
                    answer[before_idx] *= 2
            elif now == '#':
                answer[before_idx] *= -1
    
    return sum(answer)