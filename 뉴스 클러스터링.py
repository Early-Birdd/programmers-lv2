def solution(str1, str2):
    word = []
    for i in [str1, str2]:
        conv = i.upper()
        liconv = {}
        for j in range(1, len(i)):
            spword = conv[j - 1] + conv[j]
            if spword.isalpha():
                liconv[spword] = liconv.get(spword, 0) + 1

        word.append(liconv)

    s1, s2 = word
    inter = []
    for s in s1:
        if s in s2:
            inter += [s for _ in range(min(s1[s], s2[s]))]

    union = []
    check = set(list(s1) + list(s2))
    for t in check:
        union += [t for _ in range(max(s1.get(t, 0), s2.get(t, 0)))] #s1에는 있으나 s2에 없는 경우 그 반대 경우를 고려

    if len(union) != 0:
        answer = len(inter) / len(union)
    else:
        return 65536

    return int(answer * 65536)

#회고
#str1, str2를 for문에서 한번에 돌리기
#index 벗어나지 않는 팁
#dictionary get 사용법 숙지
#dictionary를 for문으로 바로 돌면 key값을 가져온다.
#dictionary에 바로 list를 씌우는 것과 빈 list를 만들어 append하는 것의 차이를 구분하기
#list에 숫자를 바로 더할 순 없지만 문자를 더하는 것은 가능하다.
#list끼리 덧셈 가능
#리스트 컴프리핸션 사용법 숙지
#교집합, 합집합 구하는 과정 생각(set활용 등)
#리스트 컴프리핸션 사용에서 min, max를 range로 감싸지 않아 에러 발생 - list에 int를 더할 수 없다.