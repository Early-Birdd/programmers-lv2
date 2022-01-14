def solution(numbers, target):
    answer = 0

    def d(L, a):
        nonlocal answer
        if L == len(numbers):
            if a == target:
                answer += 1
                return
            return

        d(L + 1, a + numbers[L])
        d(L + 1, a - numbers[L])

    d(0, 0)

    return answer

#회고
#DFS, BFS에 대한 더 깊은 이해도가 필요하다.
#두 번째 def에서는 answer에 연관된 조건확인과 연산 후 return으로 빠져나와야 한다. answer 자체를 return하는게 아니다.

#global
#ex)
# n = 1
# def f1():
#     def f2():
#         global n
#         n += 2

#nonlocal
#ex)
# def f1():
#     n = 1
#     def f2():
#         nonlocal n
#         n += 2