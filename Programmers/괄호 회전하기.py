from collections import deque

dq = None

def check():
    global dq
    stack = []

    for char in dq:
        if char in ('[', '(', '{'): stack.append(char)
        else:
            if not stack: return False
            x = stack.pop()
            if char == ']' and x != '[': return False
            elif char == ')' and x != '(': return False
            elif char == '}' and x != '{': return False
    
    return False if stack else True

def solution(s):
    global dq
    answer = 0
    for i in range(len(s)):
        dq = deque(s)
        dq.rotate(-i)
        if check(): answer += 1

    return answer