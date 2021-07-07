# 올바른 괄호 문자열 체크 
def check_proper(p):
    check = 0
    for ch in p:
        if ch == '(':
            check+=1
        elif ch == ')':
            check-=1
        if check < 0:
            return False
    return True


# 균형잡힌 괄호 문자열 u, v 로 분리
def balanced(p):
    check = 0
    u = ''
    v = ''
    for ch in p:
        u += ch
        if ch == '(':
            check += 1
        elif ch == ')':
            check -= 1
        if check == 0:
            break
    if not len(u) == len(p):
        v = p[len(u):]
    return u, v


def calc4(u, v):
    tmp = '('
    tmp += solution(v)
    tmp += ')'
    u = u[1:-1]
    for ch in u:
        if ch == '(':
            tmp += ')'
        else:
            tmp += '('
    return tmp


def solution(p):
    if not p or check_proper(p):
        return p
    
    u, v = balanced(p)
    # u가 올바른 괄호 문자열
    if check_proper(u):
        return u + solution(v)
    # u가 올바르지 않은 괄호 문자열
    else:
        return calc4(u, v)
    