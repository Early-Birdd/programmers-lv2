def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def solution(w, h):
    answer = (w * h) - (w + h - gcd(w, h))

    return answer

#회고
#수학적 아이디어를 떠올리기 힘든 문제 - 최대공약수 빼기

#더 발전된 방향
#import math -> math.gcd()

#최소공배수 (lcm)
#두 수 곱한 값을 최대공약수로 나누기