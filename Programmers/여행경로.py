from collections import defaultdict


def solution(tickets):
    path = defaultdict(list)

    for start, end in tickets:
        path[start].append(end)

    for key in path.keys():
        path[key].sort()

    answer = []
    stack = ["ICN"]
    while stack:
        airport = stack[-1]
        if path[airport] != []:
            stack.append(path[airport].pop(0))
        else:
            answer.append(stack.pop())

    return answer[::-1]
