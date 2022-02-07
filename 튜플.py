def solution(s):
    num = eval(s[1:-1])
    if len(num) > 1:
        num = sorted(num, key=lambda n: sum(n))
    else:
        return list(num)

    answer = []
    for i in num:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer

#회고
#eval : 문자열로 된 순자를 그대로 연산 가능
#{1, 2}를 []에 append 하면 [{1, 2}]
#{1, 2}에 list({1, 2})를 하면 [1, 2]
#lstrip, rstrip, split을 이용한 방법도 공부
