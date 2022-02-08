from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)]) #다리 상태를 길이에 맞춰 0으로 세팅
    time = 0
    current_weight = 0

    while len(bridge) != 0:
        out = bridge.popleft()
        current_weight -= out #다리를 지난 값을 현재 다리 위에 있는 무게에서 빼기
        time += 1
        if truck_weights:
            if current_weight + truck_weights[0] <= weight: #현재 다리 위 무게와 다음 더해질 무게를 계산
                new = truck_weights.popleft()
                current_weight += new
                bridge.append(new)
            else:
                bridge.append(0)

    return time

#회고
#다리 위 무게를 초과할 경우를 설정하기