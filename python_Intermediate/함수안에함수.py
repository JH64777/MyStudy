def outer(): # 외부 함수
    def inner(): # 내부 함수
        print("inner")
    return inner

f = outer()
f()

# =========================================

def outer2():
    num = 3
    test = 4
    def inner2():
        print(num)
        # print(test)
    return inner2

g = outer2()
g()

# outer2함수가 호출되고 끝나면 num은 사라짐
# 하지만 위 코드를 실행해 보면 3이 잘 나오는 것을 확인할 수 있음
# 이유로는 내부함수 inner2가 생성이 될 때 Enclosed function locals 영역의 변수를 
# 자신의 객체에 저장하기 때문이다

# 다음 코드로 내부함수 객체에 3이 저장되어 있는 것을 확인할 수 있다.

print(g.__closure__) # 내부 함수가 가지고 있는 객체 정보를 확인할 수 있는 코드 (각 객체들의 정보는 튜플 형식으로 저장됨)
print(g.__closure__[0].cell_contents) # 첫 번째 객체의 값 확인하는 코드

# E영역에 있는 변수 전부를 가지고 오는지 확인하기 위해 test변수를 추가해서 확인해 봤을 때
# test를 inner2에서 사용하지 않으면 추가되지 않은 것을 확인하였다.

def outer2(num): # 매개 변수 또한 E영역에 해당이 돼서 11번 줄에 있는 코드와 동일한 방식으로 운용된다
    def inner2():
        print(num)
    return inner2

g = outer2(3)
g()

