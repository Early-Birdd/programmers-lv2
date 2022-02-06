def solution(clothes):
    dic = {}
    result = 1

    for i in clothes:
        dic[i[1]] = 1
    for j in clothes:
        dic[j[1]] += 1
    for k in dic.values():
        result *= k

    return result - 1

#회고
#각 종류의 경우의 수는 사용하지 않는 것을 포함해야 하기 때문에 +1
#전체 경우의 수에서 모두 사용하지 않는 경우의 수를 빼주어야 하기 때문에 result - 1