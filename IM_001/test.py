# a = int(input())

# for _ in range(a):
#     print("start_loop")
#     N = int(input())
#     print(f'N: {N}')
#     map = [ list(map(int,input().split())) for _ in range(N) ]
#     print(map)
N = 4
print(list(map(int,input().split())) for _ in range(N) )