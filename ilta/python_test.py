import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = '서울18반_백인기'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    ###############################
    # 공 번호 i ㅡ 0(흰공), 1(1), ..., 4(4), 5(8번)
    # 공 위치 x = balls[i][0]
    # 공 위치 y = balls[i][1]
    # Data Received: 64/64/250/122/-1/-1/-1/-1/-1/-1/-1/-1/ ㅡ> (64,64),(250,122),(-1,-1),(-1,-1),(-1,-1),(-1,-1)

    '''
    1~4번 순서로 치기
    각 구멍에 대한 경로 계산, 일직선으로 불가능하면 쿠션으로 경로 계산,
    간섭이 있다면 다른 경로로 , 간섭 없는ㄷ게 없다면 다음 공으로 타겟 변경
    모든 공에 간섭이 있다면 첫 경로로 타격?
     -> 검은 공이 들어가면 패배함
      -> 최소한, 검은 공이 들어가지 않음이 확실한 경로를 선택해야함
    구멍들 좌표 데이터 HOLES
    테이블 크기 데이터 TABLE_WIDTH TABLE_HEIGHT
    공 크기 = 5.73
    '''
    white_ball_x = balls[0][0]
    white_ball_y = balls[0][1]

    i = 0

    while i < 6:
        i += 1
        if balls[i][0] == -1:
            continue

        target_ball_x = balls[i][0]
        target_ball_y = balls[i][1]

        for hole_x,hole_y in HOLES:
            # 구멍/흰공 사이값
            white_hole_diff_y = abs(white_ball_y - hole_y)
            white_hole_diff_x = abs(white_ball_x - hole_x)

            # 구멍과 흰 공 사이의 거리 계산
            white_hole_r = math.sqrt(white_hole_diff_y**2 + white_hole_diff_x**2)

            # 구멍과 흰 공이 이루는 각도 계산
            # 결과값은 라디안으로 나옴
            a_ladian_data = math.atan2(white_ball_y - hole_y,white_ball_x - hole_x)
            # 각도로 변환
            a_degrees = math.degrees(a_ladian_data)

            # 구멍/목적공 사이 거리
            target_hole_r = math.sqrt(
                (target_ball_x - hole_x)**2 + (target_ball_y - hole_y)**2
            )

            # 목적공/흰공 사이 거리
            white_target_r = math.sqrt(
                (target_ball_x - white_ball_x)**2 + (target_ball_y - white_ball_y)**2
            )

            # white_hole_r와 target_hole_r 사이 각도 구하기
            b_ladian_data = math.acos(
                (white_hole_r**2 + target_hole_r**2 - white_target_r**2) / (2 * white_hole_r * target_hole_r)
            )
            b_degrees = math.degrees(b_ladian_data)

            # 흰 공이 가야할 거리 d 구하기
            # c^2 = a^2 + b^2 + 2ab*cos
            d = math.sqrt(
                white_hole_r**2 + (target_hole_r+5.73)**2 + ( (2*white_hole_r*target_hole_r) * math.cos(b_degrees) )
            )

            # white_hole_r와 d 사이 각도 구하기
            c_ladian_data = math.acos(
                white_hole_r**2 + d **2 - (target_hole_r+5.73)**2 /(2 * white_hole_r * d)
            )
            c_degrees = math.degrees(c_ladian_data)

            # 각도는 a와 c를 합친 값
            seta = a_degrees + c_degrees

            






    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')