# def fibo(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#
#     return (fibo(n - 2) % 1234567) + (fibo(n - 1) % 1234567)
#
#
# def solution(n):
#     return fibo(n) % 1234567


def solution(n):
    fibo = [0, 1, 1]
    for i in range(3, n + 1):
        fibo.append((fibo[i - 2] + fibo[i - 1]) % 1234567)

    return fibo[n]

#회고
#재귀도 논리는 맞지만 시간에서 오답