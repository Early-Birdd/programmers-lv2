import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while True:
        min_val = heapq.heappop(scoville)
        if min_val >= K:
            return answer
        if len(scoville) == 0:
            return -1

        min_val2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min_val + min_val2 * 2)
        answer += 1

#회고
#힙의 내용 파악이 중요했던 문제, 더 깊게 공부할 것
#힙이기 때문에 첫 번째 값만 파악하면 뒤는 알아서 조건 충족
#heapq.heapify(배열)
#heapq.heappop(배열)
#heapq.heappush(배열, 값)