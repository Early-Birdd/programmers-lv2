from collections import deque

def solution(progresses, speeds):
    answer = []

    pr = deque(progresses)
    sp = deque(speeds)

    while pr:
        count = 0
        for i in range(len(pr)):
            pr[i] += sp[i]

        while pr and pr[0] >= 100:
            count += 1
            pr.popleft()
            sp.popleft()

        if count > 0:
            answer.append(count)

    return answer

#회고
#큐를 사용한 풀이, 더 깊게 공부할 필요성을 느꼈다.