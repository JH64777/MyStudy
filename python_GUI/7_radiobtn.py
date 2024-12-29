from tkinter import *

root = Tk() # 기본 GUI창에 대한 객체 생성

root.title("Nado GUI") # GUI창 제목 설정
root.geometry("640x480")

Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar() # int형으로 값을 저장한다
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치킨버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치즈버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료를 선택하세요").pack()

drink_var = StringVar() # String형으로 값을 저장
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="환타", value="환타", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()

def btncmd(): # 값 가져오는 함수
    print(burger_var.get()) # 선택된 라디오 항목의 값을(value=) 출력
    print(drink_var.get()) # 선택된 음료의 값 출력

btn = Button(root, text="주문", command=btncmd) # btncmd 함수와 연결
btn.pack()

root.mainloop()

'''
라디오 버튼은 여러가지의 선택지 중 하나를 선택할 때 이용
그룹으로 묶어주는 특징이 있어서 checkbox와는 다르게 선택한 값을 담는 변수가 그룹당 1개임
'''