### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
T = int(input())
for test_case in range(1,T+1):
    pipe = input()
































# # 테스트 케이스
# T = int(input())
# for test_case in range(1, T + 1):
#     pipe = input()
#     stack = []
#     idx_stack = []
#     pipe_stack = [ 0 for _ in range(len(pipe))]
#     cut_point = []
#     for idx,char in enumerate(pipe):
#         if char == '(':
#             stack.append(char)
#             idx_stack.append(idx)
#         elif char == ')':
#             if pipe[idx-1] == '(':
#                 cut_point.append(idx)
#             stack.pop()
#             start = idx_stack.pop()
#             end = idx
#             for i in range(start,end+1):
#                 pipe_stack[i] += 1
#
#     print(pipe_stack)
#     print(cut_point)
#     cut_pipes = []
#     for idx,cut in enumerate(cut_point):
#         if idx == 0:
#             cut_pipes.append(pipe_stack[:cut])
#
#         if idx == len(cut_point)-1:
#             cut_pipes.append(pipe_stack[cut:])
#         else:
#             cut_pipes.append(pipe_stack[cut:cut_point[idx+1]])
#
#     print(cut_pipes)
#
#
#     result = None
#     print(f"#{test_case} {result}")
