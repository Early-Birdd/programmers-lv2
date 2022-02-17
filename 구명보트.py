from collections import deque


def solution(people, limit):
    boat = 0
    people.sort()
    q = deque(people)
    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit:
                q.popleft()
                q.pop()
                boat += 1
            else:
                q.pop()
                boat += 1
        else:
            q.pop()
            boat += 1

    return boat

#회고
#큐의 특성 활용하는 아이디어
#제일 가벼운 사람과 제일 무거운 더하여 limit을 확인하고 모두 pop, 이 방식은 사람이 2명 이상 존재한다는 조건 하에 진행
#둘의 합이 limit을 넘는다면 무거운 사람만 pop
#사람이 2명 미만이라면 바로 pop