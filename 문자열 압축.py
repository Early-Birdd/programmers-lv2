def solution(s):
    answer = len(s)

    for comp in range(1, len(s) // 2 + 1):
        result = ""
        count = 1
        check = s[0:comp]
        for i in range(comp, len(s), comp):
            if check == s[i:i + comp]:
                count += 1
            else:
                if count > 1:
                    result += str(count) + check
                else:
                    result += check
                check = s[i:i + comp]
                count = 1

        if count > 1:
            result += str(count) + check
        else:
            result += check

        answer = min(answer, len(result))

    return answer

#회고
#아이디어 떠올리기가 힘든 문제
#압축의 최대길이는 전체 길이의 절반
#for문에 range가 빠졌었다.