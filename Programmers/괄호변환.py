def is_right(p):
    stack = []

    for i in range(len(p)):
        if len(stack) > 0 and p[i] == ")" and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(p[i])

    return True if len(stack) <= 0 else False


def seperate(p):
    left_count = 0
    right_count = 0
    for idx, i in enumerate(p):
        if i == "(":
            left_count += 1
        elif i == ")":
            right_count += 1

        if left_count == right_count:
            return p[: idx + 1], p[idx + 1 :]  # u,v


def batch_program(p):
    # 1번
    if p == "":
        return p
    # 2번
    u, v = seperate(p)
    # 3번
    if is_right(u):
        return u + batch_program(v)
    else:
        answer = "("
        answer += batch_program(v)
        answer += ")"

        for u_s in u[1:-1]:
            if u_s == "(":
                answer += ")"
            else:
                answer += "("
        return answer


def solution(p):
    if is_right(p):
        return p

    answer = batch_program(p)

    return answer
