from tkinter import *

root = Tk()
root.title("Label Widget")
root.geometry("300x400")

label1 = Label(root, text="안녕하세요") # Label(위치시킬 객체, text=내용)
label1.pack() # Widget 적용

photo = PhotoImage(file="python_GUI/check_box_image.png") # 이미지 객체 생성
label2 = Label(root, image=photo) # 이미지를 라벨에 적용
label2.pack()

def change():
    label1.config(text="또 만나요") # label1의 widget을 수정하는 코드

    # photo2를 global변수로 둔 이유 : 함수가 종료되면 photo2의 레퍼런스 넘버가 0이 되므로 GC의 회수 대상이 되므로 photo2가 사라지게 된다.
    # 그래서 위와 같은 이유로 전역 변수로 지정하여 GC가 회수하지 못하게 하기 위해서이다.
    # photo2가 지역변수이면 버튼을 눌렀을 때 이미지가 사라지게 된다.
    global photo2
    photo2 = PhotoImage(file="python_GUI/Not_box_image.png") # 사진 객체 생성
    label2.config(image=photo2) # 라벨의 이미지 변경

btn = Button(root, text="클릭", command=change) # 버튼 클릭시 label1의 내용을 변경하는 버튼 객체 생성
btn.pack()

root.mainloop()