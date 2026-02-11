### 제출 전에 지우기 ###
import sys
sys.stdin = open("in.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''

n, m = map(int,input().split())

a_move = [tuple(input().split()) for _ in range(n)]
b_move = [tuple(input().split()) for _ in range(m)]

from collections import deque

a_pos = deque([0])
b_pos = deque([0])

s = 0
for dr,time in a_move:
    for t in range(s,s+int(time)):
        if dr == 'R':
            a_pos.append(a_pos[t]+1)
        elif dr == 'L':
            a_pos.append(a_pos[t]-1)
    s = t

s = 0
for dr,time in b_move:
    for t in range(s,s+int(time)):
        if dr == 'R':
            b_pos.append(a_pos[t]+1)
        elif dr == 'L':
            b_pos.append(a_pos[t]-1)
    s = t

a_pos.popleft()
b_pos.popleft()

total = list(zip(a_pos,b_pos))
#print(total)
result = -1
for t,data in enumerate(total):
    if data[0] == data[1]:
        result = t + 1
print(result)