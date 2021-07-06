import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] <= K:
        if len(scoville) == 1:
            return -1
        answer += 1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        sumScoville = min1 + min2*2
        heapq.heappush(scoville, sumScoville)
        
    return answer

    '''
    heapq의 기본 모델은 최소 힙
    최대 힙으로 바꿀라면 -로 커스텀 해줘야 함.
    '''