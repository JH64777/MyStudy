from tkinter import *

root = Tk() # 기본 GUI창에 대한 객체 생성
root.title("Nado GUI") # GUI창 제목 설정
root.geometry("640x480")

Label(root, text="메뉴를 선택해 주세요").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1) # 프레임의 설정 (직선으로 영역 표시, 선 굵기를 1로)
frame_burger.pack(side="left", fill="both", expand=True) # pack에 옵션을 추가해서 해당 위젯 혹은 프레임의 위치와 차지하는 범위 등을 조정할 수 있음

Button(frame_burger, text="햄버거").pack() # 프레임에 요소 추가
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_drink = LabelFrame(root, text="음료") # 프레임이 있는 라벨 (제목이 있는 프레임이라고 생각하면 쉬울 듯)
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()
Button(frame_drink, text="환타").pack()

root.mainloop()

'''
뭔가 그룹으로 묶을 수 있는 하나의 영역을 지정하는 것이 Frame인 것 같음
'''