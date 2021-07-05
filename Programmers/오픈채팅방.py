def solution(record):
    answer = []
    change = []
    uid = {}
    for r in record:
        row = r.split(' ')
        if row[0] == 'Enter' or row[0] == 'Change':
            uid[row[1]] = row[2]
    
    for r in record:
        row = r.split(' ')
        if row[0] == 'Enter':
            answer.append(uid[row[1]] + '님이 들어왔습니다.')
        elif row[0] == 'Leave':
            answer.append(uid[row[1]] + '님이 나갔습니다.')
    
    return answer