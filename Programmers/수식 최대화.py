from itertools import permutations


def calc(exp, i, op):
    result = 0
    if op == '-':
        result = int(exp[i-1]) - int(exp[i+1])
    elif op == '+':
        result = int(exp[i-1]) + int(exp[i+1])
    else:
        result = int(exp[i-1]) * int(exp[i+1])
    return str(result)


def solution(expression):
    answer = 0
    sep_exp = []
    tmp = ''
    for i in range(len(expression)):
        if expression[i].isdecimal():
            # 숫자
            tmp += expression[i]
        else:
            # 연산자
            sep_exp.append(tmp)
            tmp = ''
            sep_exp.append(expression[i])
        if i == len(expression) - 1:
            sep_exp.append(tmp)
    print(sep_exp)
    operators = ['+', '-', '*']
    for ordered_operator in permutations(operators, 3):
        copy_exp = sep_exp[:]
        for operator in ordered_operator:
            idx = 0
            while idx < len(copy_exp):
                if copy_exp[idx] == operator:
                    result = calc(copy_exp, idx, operator)
                    del copy_exp[idx-1:idx+2]
                    copy_exp.insert(idx-1, result)
                else:
                    idx += 1
        answer = max(answer, abs(int(copy_exp[0])))
    
    return answer