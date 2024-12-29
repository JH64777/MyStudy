from tkinter import *

root = Tk() # 기본 GUI창에 대한 객체 생성

root.title("Nado GUI") # GUI창 제목 설정
root.geometry("640x480")

def createNewFile():
    print("새 파일을 만듭니다.")

# 파일 메뉴
menu = Menu(root) # 메뉴 객체 생성 (root에 소속됨)
menu_file = Menu(menu, tearoff=0) # 메뉴 버튼 아래 여러 부가적인 메뉴들을(하위 메뉴들) 추가하기 위함
menu_file.add_command(label="새 파일", command=createNewFile) # 새 파일이라는 하위 메뉴 생성 & 함수 연결
menu_file.add_command(label="새 창") # 하위 메뉴 생성
menu_file.add_separator() # 구분자를 표시하기 위한 코드
menu_file.add_command(label="파일 열기") # 하위 메뉴 생성
menu_file.add_command(label="모두 저장", state="disable") # state속성 설정으로 버튼을 비활성화 할 수 있음
menu_file.add_separator()
menu_file.add_command(label="나가기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file) # 최상단 메뉴 이름 정의 및 메뉴창에 적용

# 편집 메뉴
menu.add_cascade(label="편집") # 이렇게 cascade만 하면 상위 메뉴 버튼만 존재함

# 언어 메뉴 (메뉴에 라디오 버튼처럼 여러 선택지 중 한 가지만 선택할 수 있게 하는 방식도 적용 가능)
menu_lang = Menu(menu, tearoff=0) # tearoff가 메뉴 항목을 분리시킬 수 있게끔 할 것인지 여부를 결정하는 것 같음 (0을 쓰면 분리 안되게끔 하는 것 같음)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="언어", menu=menu_lang) # 메뉴창에 적용

# 보기 메뉴 (메뉴에서 체크박스 처럼 여러 항목을 선택할 수 있는 특징 표현 가능)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="미니맵 보기")
menu_view.add_checkbutton(label="글자 굵게")
menu_view.add_checkbutton(label="도구 표시")
menu.add_cascade(label="보기", menu=menu_view)

root.config(menu=menu)

root.mainloop()

'''
메뉴 창은 root에 소속되어 있으며
각 메뉴 항목은 메뉴창에 소속되게 코딩하는 구조를 생각하면 좋을 것 같음
'''