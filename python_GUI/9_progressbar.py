import time # 시간 딜레이를 주고자 import한 모듈
import tkinter.ttk as ttk # 프로그래스 바를 사용하기 위해 쓰는 모듈
from tkinter import *

root = Tk() # 기본 GUI창에 대한 객체 생성

root.title("Nado GUI") # GUI창 제목 설정
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 인자의 숫자ms마다 움직임 (start를 작성하면 프로그래스 바가 작동함)
# progressbar.pack()

# def btncmd(): # 값 가져오는 함수
#     progressbar.stop() # 프로그래스바 작동 중지

# btn = Button(root, text="중지", command=btncmd) # btncmd 함수와 연결
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2(): # 버튼 
    for i in range(101):
        time.sleep(0.01) # 0.01초 대기
        p_var2.set(i) # progressbar 값 설정
        progressbar2.update() # UI상으로 새롭게 변한 것을 보여주기 위해서 작성한 update코드
        print(p_var2.get()) # progressbar 값 가져오고 출력하기

btn = Button(root, text="시작", command=btncmd2) # btncmd 함수와 연결
btn.pack()

root.mainloop()