def solution(n):
    if n < 4:
        return '124'[n - 1]
    else:
        a = (n - 1) // 3
        b = (n - 1) % 3
        return solution(a) + '124'[b]

#회고
#문자열 인덱스에서 바로 뽑아쓰는 아이디어
#인덱스 지정을 위해 n - 1 설정을 유의할 것