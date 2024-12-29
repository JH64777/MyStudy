from tkinter import *

root = Tk() # 기본 GUI창에 대한 객체 생성
root.title("Nado GUI") # GUI창 제목 설정
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# yscrollcommand이 없으면 스크롤을 내려도 다시 올라온다. (만든 scroll객체의 set 메서드를 넣을 것)
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)
# listbox에 scrollbar를 매칭해준 것 같이 scrollbar에도 listbox를 매칭해줘야 한다.
# 위 코드가 없으면 휠로 동작할때는 잘 되지만 스크롤 바를 마우스로 클릭한 상태로 위 아래로 움직이는 것은 못하게 된다.

root.mainloop()