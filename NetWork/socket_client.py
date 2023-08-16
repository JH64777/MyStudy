import socket, threading

def SendMsg(clientobj): # 메시지를 보내기 위해 사용되는 함수
    while True:
        msg = input()
        if msg == "/quit": # 만일 나가고 싶다면 해당 명령어를 사용하면 된다.
            clientobj.close()
        else:
            clientobj.send(msg.encode("utf-8")) # 메시지를 보내기 위한 부분 
            # (Encoding을 하는 이유는 문자열로 받은 데이터는 파이썬의 문자열 객체로 인식이 되기 때문에 객체가 아닌 날 것의 데이터로 보내기 위함)

def RecieveMsg(clientobj): # 메시지를 받기 위해 사용되는 함수
    while True:
        print("상대측 : " + clientobj.recv(1024).decode("utf-8")) # 메시지를 받기 위한 부분, 최대 1024bytes의 크기를 받겠다는 의미
        # (더 큰 값을 보낼 시 나머지 데이터는 다음에 받는 코드가 실행 될 때 받음)
        # 해당 코드도 Decoding하는 이유가 상대측에서 보내는 메시지가 인코딩 된 상태의 데이터이므로 우리가 읽을 수 있게끔 디코딩 하는 것임(인코딩의 역 동작이 디코딩)

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓을 생성 : IPv4방식의 TCP방식으로 메시지를 처리하는 소켓을 생성한다는 의미

try: # 서버가 연결 준비를 됐다면(서버가 구동되어 있다면)
    ClientSocket.connect(("127.0.0.1", 8080)) # 해당 IP주소의 8080번의 포트번호로 연결을 시도하겠다는 의미
    print("연결을 성공적으로 했습니다!")
    t1 = threading.Thread(target=SendMsg, args=(ClientSocket,)) # 메시지를 보내는 일을 처리하는 서브 쓰레드 객체 생성
    t2 = threading.Thread(target=RecieveMsg, args=(ClientSocket,)) # 메시지를 받는 일을 처리하는 서브 쓰레드 객체 생성
    t1.start() # 쓰레드 실행
    t2.start() # 쓰레드 실행
    
except: # 서버가 연결 준비가 안됐다면
    print("연결을 할 수 없습니다.")
