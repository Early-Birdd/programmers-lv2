def re(u):
    result = ""

    for i in u:
        if i == '(':
            result += ')'
        else:
            result += '('

    return result


def right(u):
    stack = []

    for i in u:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) == 0:
        return True
    else:
        return False


def divide(p):
    o = 0
    c = 0

    for i in range(len(p)):
        if p[i] == '(':
            o += 1
        else:
            c += 1

        if o == c and o + c < len(p):
            return p[:i + 1], p[i + 1:]

    return p, ""


def answer(p):
    if p == "":
        return ""

    u, v = divide(p)

    if right(u):
        return u + answer(v)
    else:
        u = u[1:-1]
        return '(' + answer(v) + ')' + re(u)


def solution(p):
    return answer(p)

#회고
#re함수 안 for문 if 조건에서 i == 이 아닌 u == 이라는 실수를 하였다... 오타를 항상 조심할 것
#상황에 맞는 새 함수를 구현할 것
#range 초과할 때의 경우를 고려하기
#[:a] => a-1 까지라는 것을 망각하지 말기
