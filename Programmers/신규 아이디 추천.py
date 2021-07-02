def solution(new_id):
    answer = new_id
    # step1
    answer = answer.lower()
    # step2
    characters = '-_.'
    answer = ''.join(x for x in answer if x.isalnum() or x in characters)
    # step3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # step4
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    # step5
    if not answer: answer = 'a'
    # step6
    if len(answer)>=16:
        answer = answer[:15]
        if answer[-1]=='.':
            answer = answer[:-1]
    # step7
    while len(answer) <= 2:
        answer += answer[-1]
    
    return answer