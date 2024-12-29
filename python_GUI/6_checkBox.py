from tkinter import *

root = Tk() # 기본 GUI창에 대한 객체 생성

root.title("Nado GUI") # GUI창 제목 설정
root.geometry("640x480")

chkvar = IntVar() # chkvar에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() # 체크박스 선택된 상태로 변경하는 코드
# chkbox.deselect() # 체크박스 선택되지 않은 상태로 변경하는 코드
chkbox.pack()

chkvar2 = IntVar() # chkbox2의 상태값을 저장하는 변수
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd(): # 값 가져오는 함수
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd) # btncmd 함수와 연결
btn.pack()

root.mainloop()
