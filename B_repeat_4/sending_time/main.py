import sys

from solution import init, addLine, removeLine, checkTime

CMD_INIT = 0
CMD_ADD = 1
CMD_REMOVE = 2
CMD_CHECK = 3

MAX_LINE = 30000

nodeA = [0 for _ in range(MAX_LINE)]
nodeB = [0 for _ in range(MAX_LINE)]
Time = [0 for _ in range(MAX_LINE)]


def run():
    input_iter = iter(input().split())
    Q = int(next(input_iter))
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            K = int(next(input_iter))
            for i in range(0, K):
                input_iter = iter(input().split())
                nodeA[i] = int(next(input_iter))
                nodeB[i] = int(next(input_iter))
                Time[i] = int(next(input_iter))
            init(N, K, nodeA, nodeB, Time)
            okay = True
        elif cmd == CMD_ADD:
            node_a = int(next(input_iter))
            node_b = int(next(input_iter))
            time = int(next(input_iter))
            addLine(node_a, node_b, time)
        elif cmd == CMD_REMOVE:
            node_a = int(next(input_iter))
            node_b = int(next(input_iter))
            removeLine(node_a, node_b)
        elif cmd == CMD_CHECK:
            node_a = int(next(input_iter))
            node_b = int(next(input_iter))
            ret = checkTime(node_a, node_b)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        else:
            okay = False
    return okay


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    T, MARK = map(int, input().split())

    for tc in range(1, 1 + 1):
        score = MARK if run() else 0
        print("#%d %d" % (tc, score), flush=True)