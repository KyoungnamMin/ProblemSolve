def solution(number, k):
    stack = []
    for i, n in enumerate(number):
        while stack and n > stack[-1] and k>0:
            k-=1
            stack.pop()
        if k == 0:
            stack.extend([x for x in number[i:]])
            break
        stack.append(n)
    
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)