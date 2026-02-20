from collections import deque
 
maps = {
    0 : '+',
    1 : '-',
    2 : '*',
    3 : '/',
}
 
def permutations(oper_arr, number_q, n, N, values):
    if n == N-1:
        values['max_reward'] = max(values['max_reward'], number_q[0])
        values['min'] = min(values['min'], number_q[0])
        return
    for i in range(4):
        if oper_arr[i] == 0: continue
        oper_arr[i] -= 1
        n1 = number_q.popleft()
        n2 = number_q.popleft()
 
        if maps[i] == '+':
            number_q.appendleft(n1+n2)
        elif maps[i] == '-':
            number_q.appendleft(n1-n2)
        elif maps[i] == '*':
            number_q.appendleft(n1 * n2)
        else:
            number_q.appendleft(int(n1/n2))
        permutations(oper_arr, number_q, n+1, N, values)
        number_q.popleft()
        number_q.appendleft(n2)
        number_q.appendleft(n1)
        oper_arr[i] += 1
 
 
def solve():
    T = int(input())
    for test_case in range(1, T + 1):
        N = int(input())
        oper_arr = list(map(int, input().split()))
        number_arr = list(map(int, input().split()))
        number_q = deque(number_arr)
        values = {
            'max_reward' : -float('inf'),
            'min' : float('inf')
        }
        permutations(oper_arr, number_q, 0, N, values)
        print(f"#{test_case} {values['max_reward']-values['min']}")
 
solve()