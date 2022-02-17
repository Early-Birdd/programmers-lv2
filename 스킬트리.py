# def solution(skill, skill_trees):
#     answer = 0
#
#     for sk in skill_trees:
#         include = 0
#         seq = 0
#
#         for i in range(len(sk)):
#             if sk[i] in skill:
#                 include += 1
#             if seq < len(skill) and sk[i] == skill[seq]:
#                 seq += 1
#         if include == seq:
#             answer += 1
#
#     return answer

def solution(skill, skill_trees):
    answer = 0

    for sk in skill_trees:
        skill_copy = ''
        for i in range(len(sk)):
            if sk[i] in skill:
                skill_copy += sk[i]
        if skill_copy == skill[0:len(skill_copy)]:
            answer += 1

    return answer

#회고
#1번 - seq가 범위를 벗어나는 경우를 설정하지 않아 에러가 났다.
#2번 - 모든 스킬을 배우지 못한 경우 즉 CBD 스킬트리 중 CB까지만 배우고 끝날 수 있으므로 [0:len(skill_copy]