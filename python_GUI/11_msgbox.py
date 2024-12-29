import tkinter.messagebox as msgbox # 메시지 박스를 사용하기 위해 import하는 모듈
from tkinter import *

root = Tk() # 기본 GUI창에 대한 객체 생성
root.title("Nado GUI") # GUI창 제목 설정
root.geometry("640x480")

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.") # (타이틀, 내용) 정보 전달을 위해 사용 - showinfo

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.") # (타이틀, 내용) 경고를 위해 사용 - showwarning

def error():
    msgbox.showerror("에러", "결제 오류가 발생했습니다.") # (타이틀, 내용) 에러를 나타내기 위해 사용 - showerror

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 죄석은 유아동반석입니다. 예매하시겠습니까?") # (타이틀, 내용) 사용자의 선택을 묻기 위해 사용 - askokcancel

def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?") # (타이틀, 내용) 사용자에게 재시도를 묻기 위해 사용 - askretrycancel
    print(response) # 재시도 True, 취소 False

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?") # (타이틀, 내용) 사용자의 선택을 묻기 위해 사용 - askyesno

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다. \n저장하시겠습니까?") # (타이틀, 내용) 사용자의 선택을 묻기 위해 사용 - askyesnocancel
    # 알림창의 제목이 없이 화면에 보이고 싶다면 title속성에 None 값을 넣으면 된다.
    print("응답 : ", response) # 변수에다가 물음에 대한 답의 값을 저장할 수 있음 -> 예 True, 아니오 False, 취소 None
    if response == 1: # 숫자로도 처리 가능
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()
