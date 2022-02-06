def solution(numbers):
    result = []

    for i in numbers:
        result.append(str(i))

    result.sort(key=lambda x: x * 3, reverse=True)

    return str(int(''.join(result)))

#회고
#sort lambda 사용법 숙지하기
#list(map(str, numbers) 생각해보기
#.sort()는 갱신x
#sorted()는 갱신 필요