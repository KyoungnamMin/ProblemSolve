def solution(absolutes, signs):
    answer = [value if sign == True else -value for value, sign in zip(absolutes, signs)]
    return sum(answer)