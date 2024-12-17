# TCP/IP 서버
import socket, threading

def SendMsg(sendobj): # 메시지를 보내기 위한 함수 매개변수로 클라이언트 소켓 객체를 받음
    while True:
        msg = input()
        if msg == "/shutdown": # 서버 종료 명령어
            sendobj.close()
        elif msg == "/showuser": # 현재 접속중인 클라이언트 정보
            print(f"현재 접속 인원 : {sendobj}")
        else:
            sendobj.send(msg.encode("utf-8")) 
            # 보낼 메시지를 encoding 하는 이유는 input으로 받은 문자열이 python에서 제공하는 문자열 객체라서 날 것의 데이터로 변경해서 보내야 하기 때문

def RecieveMsg(sendobj):
    while True:
        print("상대측 : " + sendobj.recv(2).decode("utf-8")) # 최대 받는 크기를 1024byte 만큼 받겠다는 의미 1024보다 높으면 다음에 받을 때 마저 받게 됨
    # 여기도 decoding을 하는 이유는 아까 데이터를 보낼 때 encoding을 했기 때문에 사용자가 읽을 수 있는 방식으로 다시 돌려놓기 위함

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET : IPv4 방식을 의미, SOCK_STREAM : TCP 방식을 의미
# 즉 IPv4방식의 TCP 방식으로 소통하는 소켓을 생성한다는 뜻

serversocket.bind(("127.0.0.1", 8080)) # 소켓이 통신할 때 해당 IP주소와 포트번호를 사용한다는 뜻

serversocket.listen(1) # 매개변수 값 만큼의 연결 요청을 큐에 넣는다는 것을 의미
print("수신 대기 중")
ClientSocket, ClientIP = serversocket.accept() # 클라이언트의 요청에 대해서 연결 허락을 하는 메서드로 클라이언트의 소켓 정보, IP정보에 대한 값을 반환
print(f"상대측에서 접속을 했습니다! : {ClientIP}")

t1 = threading.Thread(target=SendMsg, args=(ClientSocket,)) # 서브 쓰레드 객체를 생성 및 해당 쓰레드가 어떤 코드를 작동시킬 것인지 지정
t2 = threading.Thread(target=RecieveMsg, args=(ClientSocket,))

t1.start() # t1 쓰레드 객체 시작
t2.start() # t2 쓰레드 객체 시작