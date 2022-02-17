# from collections import deque
# def solution(priorities, location):
#     answer = []
#     que = deque(priorities)
#     que_i = deque(range(len(priorities)))
#     curr = 0
#     while len(que):
#         curr = que.popleft()
#         if len(que) == 0:
#             answer.append(que_i.popleft())
#             break
#
#         if curr < max(que):
#             que.append(curr)
#             que_i.append(que_i.popleft())
#         elif curr >= max(que):
#             answer.append(que_i.popleft())
#         print(que, answer)
#
#
#     return answer.index(location)+1
#
#
# from collections import deque
#
#
# def solution(priorities, location):
#     answer = 0
#
#     index_list = deque(i for i in range(len(priorities)))
#     maxi = max(priorities)
#
#     while True:
#         index = index_list.popleft()
#         if priorities[index] < maxi:
#             index_list.append(index)
#         else:
#             answer += 1
#             priorities[index] = 0
#             maxi = max(priorities)
#             if index == location:
#                 return answer

# from collections import deque
#
#
# def solution(priorities, location):
#     answer = 0
#
#     q = deque(priorities)
#     index = deque(i for i in range(len(q)))
#
#     while q:
#         qq = q.popleft()
#         if len(q) == 0:
#             return answer + 1
#
#         if qq < max(priorities):
#             q.append(qq)
#             index.append(index.popleft())
#         else:
#             answer += 1
#             check = index.popleft()
#             if check == location:
#                 return answer
#
# priorities = [1, 1, 9, 1, 1, 1]
# location = 0
#
# print(solution(priorities, location))