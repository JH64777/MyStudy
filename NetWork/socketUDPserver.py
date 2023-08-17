# UDP 방식 소켓 통신 (서버)
import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # udp 소켓 생성 | 의미 : IPv4와 UDP 방식으로 통신하는 소켓을 생성하겠다.

serverSocket.bind(("127.0.0.1", 8080)) # 소켓에 IP, Port정보 적용

while True:
    try:
        data, addr = serverSocket.recvfrom(2) # udp식 데이터 받기 크기는 테스트를 위해 2bytes로 설정
        print(f"받은 데이터 : {data}") # 정상적으로 받으면 데이터 출력
    except Exception as error: # 모든 예외 상황 발생 시 error변수에 발생한 에러코드를 저장
        print(f"에러 발생:{error}") # 에러 출력
