def solution(s):
    stack = []

    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        return 1

    else:
        return 0

#회고
#stack의 활용을 생각하지 못하고 문자열 바꾸기 replace에 집중하여 해답을 찾지 못하였다.
#stack의 마지막을 확인해보는 [-1]을 잘 활용하자.