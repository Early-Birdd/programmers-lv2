def solution(record):
    answer = []

    database = {}

    for first in record:
        check = first.split()
        if check[0] == "Enter" or check[0] == "Change":
            database[check[1]] = check[2]

    for impl in record:
        check_2 = impl.split()
        if check_2[0] == "Enter":
            answer.append(database[check_2[1]] + "님이 들어왔습니다.")
        elif check_2[0] == "Leave":
            answer.append(database[check_2[1]] + "님이 나갔습니다.")

    return answer

#회고
#for문 2개 사용으로 간단하게 해결하기 - 기록할 이름은 들어올 때와 바꿀 때
#answer가 문자열이 아닌 배열인데 +를 사용해버려 에러, append 사용하기