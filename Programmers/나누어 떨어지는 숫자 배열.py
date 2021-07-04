def solution(arr, divisor):
    answer = sorted([v for v in arr if v%divisor==0])
    if len(answer) == 0:
        answer.append(-1)
    return answer