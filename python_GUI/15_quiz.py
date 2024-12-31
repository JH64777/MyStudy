from tkinter import *

def OpenFile():
    try:
        with open("./mynote.txt", "r") as f:
            s = f.read()
            textbox.delete("1.0", END)
            textbox.insert(END, s)
    except Exception:
        print("Error!")

def SaveFile():
    try:
        with open("./mynote.txt", "w") as f:
            f.write(textbox.get("1.0", END))
    except Exception:
        print("Error!")

main = Tk()

main.title("제목 없음 - Windows 메모장")
main.geometry("640x480")

menu = Menu(main)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=OpenFile)
menu_file.add_command(label="저장", command=SaveFile)
menu_file.add_command(label="끝내기", command=main.quit)
menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

main.config(menu=menu)

scroll = Scrollbar(main)
scroll.pack(side="right", fill="y")

textbox = Text(main, yscrollcommand=scroll.set)
textbox.pack(side="left", fill="both", expand=True)

scroll.config(command=textbox.yview)

main.mainloop()