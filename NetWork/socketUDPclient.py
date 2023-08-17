# UDP 방식 소켓통신 (클라이언트)
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # udp 소켓 생성

sIP = "127.0.0.1" # 서버에 대한 IP 정보
sPort = 8080 # 서버의 포트번호

while True:
    msg = input(">>> ") # 보낼 메시지 입력
    clientSocket.sendto(msg.encode("utf-8"), (sIP, sPort)) # 메시지 전송

