import tkinter.ttk as ttk # 콤보박스는 해당 모듈에 있어서 추가적으로 import 해줘야함
from tkinter import *

root = Tk() # 기본 GUI창에 대한 객체 생성

root.title("Nado GUI") # GUI창 제목 설정
root.geometry("640x480")

# Readonly 적용 X
values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values) # height의 값이 콤보박스 선택 시 보여주는 요소의 최대 갯수를 의미함
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정하는 코드

# Readonly 적용 O
readOnlyCombobox = ttk.Combobox(root, height=10, values=values, state="readonly") # state값을 추가하여 콤보박스에 다른 값을 입력하는 것을 방지할 수 있음
readOnlyCombobox.current(0) # 0번째 값을 선택한 상태로 시작하게 설정
readOnlyCombobox.pack()


def btncmd(): # 값 가져오는 함수
    print(combobox.get()) # 선택된 값을 출력
    print(readOnlyCombobox.get())

btn = Button(root, text="선택", command=btncmd) # btncmd 함수와 연결
btn.pack()

root.mainloop()