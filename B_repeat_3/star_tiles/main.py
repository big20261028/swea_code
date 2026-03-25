import sys

from solution import init, getCount, getPosition

CMD_INIT = 0
CMD_CNT = 1
CMD_POSITION = 2

MAX_SIZE = 1000

Map = [[0 for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]
Piece = [[0 for _ in range(5)] for _ in range(5)]
Data = [0 for _ in range(40000)]

def init_map(N : int):
    global Map, Data
    idx = 0
    x = 0
    for i in range(int(N / 25)):
        for y in range(N):
            data = Data[idx]
            idx = idx + 1
            bit = 1
            for m in range(25):
                if data & bit != 0:
                    Map[y][x + m] = 1
                else:
                    Map[y][x + m] = 0
                bit = bit * 2
        x = x + 25

    dcnt = N % 25
    if dcnt != 0:
        for y in range(N):
            data = Data[idx]
            idx = idx + 1
            bit = 1
            for m in range(dcnt):
                if data & bit != 0:
                    Map[y][x + m] = 1
                else:
                    Map[y][x + m] = 0
                bit = bit * 2


def make_piece(data : int):
    global Piece
    bit = 1
    for i in range(5):
        for k in range(5):
            if data & bit != 0:
                Piece[i][k] = 1
            else:
                Piece[i][k] = 0
            bit = bit * 2

def run():
    global Map, Data, Piece
    input_iter = iter(input().split())
    Q = int(next(input_iter))
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            cnt = int(next(input_iter))
            for i in range(0, cnt):
                input_iter = iter(input().split())
                Data[i] = int(next(input_iter))
            init_map(N)
            init(N, Map)
            okay = True
        elif cmd == CMD_CNT:
            Data[0] = int(next(input_iter))
            make_piece(Data[0])
            ans = int(next(input_iter))
            ret = getCount(Piece)
            if ret != ans:
                print('cnt Fail')
                okay = False
        elif cmd == CMD_POSITION:
            row = int(next(input_iter))
            col = int(next(input_iter))
            ret = getPosition(row, col)
            ans = int(next(input_iter))
            if ret != ans:
                #print('position Fail')
                okay = False
        else:
            okay = False
    return okay


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    T, MARK = map(int, input().split())

    for tc in range(1, T + 1):
        score = MARK if run() else 0
        print("#%d %d" % (tc, score), flush=True)