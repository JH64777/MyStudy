from tkinter import *

root = Tk() # 기본 GUI창에 대한 객체 생성

root.title("Nado GUI") # GUI창 제목 설정
root.geometry("640x480")

txt = Text(root, width=30, height=5) # text 박스 객체 생성 (너비 30, 높이 5)
txt.pack()
txt.insert(END, "글자를 입력하세요") # text박스 widget에 글자를 넣은 메서드

e = Entry(root, width=30) # Entry 박스 객체 생성
e.pack()
e.insert(0, "한 줄만 입력해요") # 0 대신 END를 써도 무방(단, 글자가 없을 때)

def btncmd(): # 값 가져오는 함수 및 내용 지우기

    # 값 가져오기
    print(txt.get("1.0", END)) # txt박스에 있는 내용을 가져오려면 get메서드를 사용해야 한다 
    # get메서드의 인자 값 의미 1은 라인 1부터, 0은 라인 기준으로 처음 위치부터(1번 줄의 처음 부분, 2번 줄의 처음 부분 등) 가져와라
    print(e.get()) # Entry 박스에 있는 값을 가져오는 메서드

    # 내용 지우기
    txt.delete("1.0", END) # 1번째 줄 0번째 글자 부터(처음부터) 끝까지 지워라
    e.delete(0, END) # 처음부터 끝까지 지워라

btn = Button(root, text="클릭", command=btncmd) # btncmd 함수와 연결
btn.pack()

root.mainloop()

'''
Entry 박스와 Text박스의 차이점
- Entry : 한 줄만 입력 가능
- Text : 여러 줄에 입력이 가능하다
'''