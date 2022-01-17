def solution(rows, columns, queries):
    answer = []
    li = [[0] * (columns + 1) for _ in range(rows + 1)]
    check = 1

    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            li[i][j] = check
            check += 1

    for q in queries:
        a, b, c, d = q
        tmp = li[a][b]
        min_v = tmp
        for x in range(a, c):
            li[x][b] = li[x + 1][b]
            min_v = min(min_v, li[x][b])

        for x in range(b, d):
            li[c][x] = li[c][x + 1]
            min_v = min(min_v, li[c][x])

        for x in range(c, a, -1):
            li[x][d] = li[x - 1][d]
            min_v = min(min_v, li[x][d])

        for x in range(d, b, -1):
            li[a][x] = li[a][x - 1]
            min_v = min(min_v, li[a][x])

        li[a][b + 1] = tmp
        answer.append(min_v)

    return answer

#회고
#시작 전 첫 행 첫 열을 미리 저장하고 실행 후 그 값을 한 칸 오른쪽으로 넣어 완성 시키는 전략
#각 실행에서 미리 저장한 값과의 비교
#오른쪽 세로와 위쪽 가로에서 아래와 같이 구현하였었는데 이런식으로 하면 다음 값이 미리 갱신되어버려 에러가 난다.
#해당 구간에서는 for문에서 뒤로 도는 전략 사용
# for x in range(a, c):
#     li[x + 1][d] = li[x][d]
#     min_v = min(min_v, li[x][d])
#
# for x in range(b, d):
#     li[a][x + 1] = li[a][x]
#     min_v = min(min_v, li[a][x])
