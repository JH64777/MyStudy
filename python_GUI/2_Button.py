from tkinter import *

root = Tk()
root.title("Button Widget")
root.geometry("300x400")

btn1 = Button(root, text="버튼1") # Button(어디에 위치 시킬 것인지, 버튼에 보일 내용)
# root라는 창 객체에다가 버튼을 새롭게 만들 것이므로 root 객체를 인자로 넘겼다.
btn1.pack() # 해당 코드가 있어야지 btn1이 실제적으로 root 창에 적용이 됨

btn2 = Button(root, padx=5, pady=10, text="버튼2222222") # padding x, padding y를 조절할 수 있음
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼444444444444") # 버튼 위젯 자체의 크기를 직접 설정한 것
btn4.pack()

'''
padding과 크기 설정의 차이점
- padding : widget 안에 들어가는 글자 내용이 커지면 글자의 길이 만큼 widget도 같이 커짐
- 직접 크기 설정 : widget안에 들어가는 글자 내용이 커지면 크기는 고정이 되어서 글자가 짤림
'''

btn5 = Button(root, fg="red", bg="black", text="버튼5") # 위젯의 foreground(글자), background(버튼 색)를 원하는 색으로 지정할 수 있음
btn5.pack()

photo = PhotoImage(file="python_GUI/check_box_image.png") # 특정 경로에 있는 이미지를 가져오는 코드
btn6 = Button(root, image=photo) # Button을 만들때 image인자에 위에서 만든 이미지 객체를 넣으면 불러온 이미지를 버튼에 적용시킨다.
btn6.pack()

def btncmd(): # 버튼이 클릭되었을 때 호출할 함수
    print("버튼이 클릭되었어요")

btn7 = Button(root, text="동작하는 버튼", command=btncmd) # command인자에 함수를 넣어서 버튼이 클릭되었을 때 함수가 호출되도록 연결해줄 수 있다
btn7.pack()

root.mainloop()