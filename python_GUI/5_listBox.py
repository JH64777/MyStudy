from tkinter import *

root = Tk() # 기본 GUI창에 대한 객체 생성

root.title("Nado GUI") # GUI창 제목 설정
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0) # 여러 가지 값들을 한번에 볼 수 있게끔 하는 목록 Widget
'''
selectmode 옵션
 - extended : 여러 개의 목록 선택 가능하게 설정
 - single : 하나의 목록만 선택 가능 설정

hegith 옵션
 - 0 : 현재 있는 목록을 전부 보여줌
 - 1 : 목록 1개만 보여줌
 - 2 : 목록 2개 ...
* 아래 방향키를 사용해서 아래 숨겨진 목록들을 확인할 수 있음 *
'''

listbox.insert(0, "사과") # 0번 순서에 "사과"라는 값 추가
listbox.insert(1, "딸기") # 1번 순서에 ...
listbox.insert(2, "바나나")
listbox.insert(END, "수박") # END 키워드를 통해서도 추가 가능 (단 마지막 인자 다음에 추가함 여기서는 3 인덱스가 됨)
listbox.insert(END, "포도") # 여기서도 END 키워드 통해서 마지막에 값 추가 (여기서는 인덱스가 4가 됨)
listbox.pack()


def btncmd(): # 값 가져오는 함수 및 내용 지우기
    # listbox.delete(END) # 맨 마지막 목록 삭제
    # listbox.delete(0) # 가장 처음 목록 삭제

    # 갯수 확인
    print("리스트에는", listbox.size(), "개가 있습니다") # 리스트의 총 목록 갯수 확인

    # 항목 확인
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2)) # 0번 인덱스 ~ 2번 인덱스까지의 값을 가져오는 메서드

    # 선택된 항목 확인 (인덱스 값으로 확인)
    print("선택된 항목 : ", listbox.curselection()) # 선택된 항목의 인덱스 값 확인

btn = Button(root, text="클릭", command=btncmd) # btncmd 함수와 연결
btn.pack()

root.mainloop()

'''
Entry 박스와 Text박스의 차이점
- Entry : 한 줄만 입력 가능
- Text : 여러 줄에 입력이 가능하다
'''