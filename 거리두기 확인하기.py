def check(p, save_P):
    for a in save_P:
        for b in save_P:
            x1, y1, x2, y2 = a[0], a[1], b[0], b[1]
            mh = abs(x1 - x2) + abs(y1 - y2)
            if mh == 0:
                continue
            elif mh == 1:
                return 0
            elif mh == 2:
                if x1 == x2:
                    if p[x1][(y1 + y2) // 2] == 'O':
                        return 0
                elif y1 == y2:
                    if p[(x1 + x2) // 2][y1] == 'O':
                        return 0
                else:
                    if p[x1][y2] == 'O':
                        return 0
                    elif p[x2][y1] == 'O':
                        return 0

    return 1


def solution(places):
    answer = []

    for i in range(5):
        save_P = []
        p = places[i]
        for j in range(5):
            pp = p[j]
            for k in range(5):
                ppp = pp[k]
                if ppp == 'P':
                    save_P.append((j, k))

        answer.append(check(p, save_P))

    return answer

#회고
#각 P의 위치를 저장할 방법 생각하기
#행렬을 계속 생각하다가 p[x1, (y1 + y2) // 2] 로 표현하여 에러가 났다. [][]로 해야했다.