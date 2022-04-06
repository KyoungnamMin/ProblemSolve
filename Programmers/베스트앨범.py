from collections import defaultdict


def solution(genres, plays):
    answer = []

    genre_list = defaultdict(list)
    total_play = defaultdict(int)

    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_list[g].append((i, p))
        total_play[g] += p

    for (k, v) in sorted(total_play.items(), key=lambda x: x[1], reverse=True):
        for (i, p) in sorted(genre_list[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
