def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            j = yellow // i
            if ((i + 2) * (j + 2)) - (i * j) == brown:
                return [max(i + 2, j + 2), min(i + 2, j + 2)]

#회고
#규칙을 잘 생각하자
#약수를 활용할 것
#가로는 세로보다 길거나 같기 때문에 max, min을 활용