def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)

    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)

#회고
#while 대신 if를 사용하면 먼저 스택에 쌓여있던 작은 수를 제거할 수 가 없다
#k != 0 이 부분은 "4321" 처럼 k를 다 사용하지 못한 경우 즉각 제거를 위해 사용해야 한다.
#문자열도 비교가 가능하다는 것을 숙지