from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        check = []
        for o in orders:
            check += combinations(sorted(o), c)
        if check:
            m = max(Counter(check).values())
            for k, v in Counter(check).items():
                if v >= 2 and v == m:
                    answer.append("".join(k))

    answer.sort()

    return answer

#회고
#문자열은 sorted(~) 사용, .sort() 불가
#sorted()는 출력 시 따로 갱신을 해야하고 .sort()는 자동갱신
#"~".join -> 문자 리스트 각 사이에 ~를 삽입
#combinations는 []에 append말고 +로 삽입
#[]가 비어있으면 false, 요소가 있으면 true
#[]가 비어있으면 max() 불가능
