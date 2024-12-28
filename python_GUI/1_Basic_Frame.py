from tkinter import *

root = Tk() # 기본 GUI창에 대한 객체 생성

# root2 = Tk()
# root2.title("Second GUI")
# 여기 주석을 제거하고 실행해보면 Second GUI라는 제목을 가진 기본 창이 하나 더 생성됨을 확인할 수 있음

root.title("Nado GUI") # GUI창 제목 설정
root.geometry("640x480+200+300") # 가로크기*세로 크기+x좌표+y좌표 (x좌표와 y좌표는 굳이 안써도 실행됨)
# 좌측 상단부터가 시작지점으로 x좌표가 커질수록 오른쪽으로 이동하고 y좌표가 커질수록 아래로 내려간다

root.resizable(True, False) # 너비, 높이 크기조정 불가

root.mainloop() # 윈도우가(GUI창이) 종료될 때까지 실행시키는 메서드
