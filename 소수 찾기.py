main_set = set()

def check(combi):
    if combi in (0, 1):
        return False

    n = int(combi ** 0.5)

    for i in range(2, n + 1):
        if combi % i == 0:
            return False

    return True


def recursive(combi, others):
    print(combi)
    if combi != "":
        if check(int(combi)):
            main_set.add(int(combi))

    for i in range(len(others)):
        recursive(combi + others[i], others[:i] + others[i + 1:])


def solution(numbers):
    recursive("", numbers)

    return len(main_set)

#회고
#set을 활용할 것
#[i:] 와 [:i]의 결과를 잘 생각할 것 [i]하였을 때의 범위 초과에러와 다르다.