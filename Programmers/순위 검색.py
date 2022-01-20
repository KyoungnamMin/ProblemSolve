from collections import defaultdict
from bisect import bisect_left


def parse_info(info):
    info = info.split(" ")
    info_key = []
    info_value = int(info[-1])

    for i in (info[0], "-"):
        for j in (info[1], "-"):
            for k in (info[2], "-"):
                for l in (info[3], "-"):
                    info_key.append(i + j + k + l)

    return info_key, info_value


def parse_query(q):
    q = q.replace("and ", "").split(" ")
    v = int(q[-1])
    return "".join(q[:-1]), v


def solution(infos, query):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        keys, value = parse_info(info)
        for key in keys:
            info_dict[key].append(value)

    for k in info_dict.keys():
        info_dict[k].sort()

    for q in query:
        q_key, q_value = parse_query(q)
        scores = info_dict[q_key]
        bis = bisect_left(scores, q_value)
        answer.append(len(scores) - bis)
    return answer
