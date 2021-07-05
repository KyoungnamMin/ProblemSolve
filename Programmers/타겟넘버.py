answer = 0
def dfs(numbers, target, calc, count):
    global answer
    if count==len(numbers):
        if calc==target:
            answer += 1
        return
    dfs(numbers, target, calc+numbers[count], count+1)
    dfs(numbers, target, calc-numbers[count], count+1)
    

def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer