'''
파이썬 변수에 값을 바인딩 하거나 변수의 값을 참조하는 경우 따르는 규칙들
L(Local) : 함수 안쪽을 의미
E(Enclosed Function Locals) : 내부 함수에서 자신의 외부 함수의 범위
G(Global) : 함수 바깥 부분, 모듈 범위
B(Built-in) : open, range와 같은 파이썬 내장 함수들
'''

# 파이썬에서 어떤 변수가 바인딩 하는 값을 참조하는 경우 LEGB 순으로 탐색을 한다

a = 10 # Global 영역

def test(): # Local 영역
    a = 20
    print(a)

test() # L, E, G, B 순으로 탐색하는 것이므로 20 출력

b = 10 # global

def test2(): # local
    print(b)

test2() # 10 출력
'''
먼저 Local 영역을 확인하여 b를 찾고 없어서 다음으로
Enclosed Function Locals 부분을 찾는데 해당 영역 자체가 없어서
다음 영역인 Global 영역을 찾은 결과 b라는 변수가 있으므로 10을 출력한다
'''

c = 30 # Global

def test3(): # Local
    c = 20
    print(c)

test3() # 20
print(c) # 30

'''
test3()같은 경우 함수가 호출이 되며 c라는 변수가 바인딩 되고 c가 출력될 때
c는 L에 있으므로 20이 출력이 된다

하지만 global 영역에 있는 print(c)는 함수가 호출되고 종료된 시점이기 때문에
함수 안에서 선언된 c는 이미 소멸을 하였기에 L영역은 사라지게 되며
G영역에 있는 c가 호출이 되어서 30을 출력해낸다
'''

d = 22

print(d) # d 값 수정 전 출력

def changeGlob(): # Local 영역에서 Global 변수를 바꾸는 함수
    global d # 전역변수의 값을 수정하고 싶다면 변수 앞에 global 키워드를 붙이고 이후에 수정하면 된다
    d = 33 # 전역변수 d의 값 수정

changeGlob() # 함수 호출
print(d) # d 값 출력

'''
궁금한 점
과연 함수 안에 변수 d를 추가하고 global 키워드를 써서
전역변수 한 번 지역 변수 한 번 수정하고 싶으면 어떻게 해야 할까?
'''

# 방법 1
# name = "Sheep"

# def Test(newName):
#     name = "James"
#     global name
#     name = newName
# 위 방법으로는 name" is assigned before global declaration 에러가 뜬다

# 방법 2
name = "Sheep"

def PrintName(newName):
    name = "Null" # 로컬 변수 name
    ChangeGlob(newName) # 글로벌 변수 변경
    name = "Hello"
    print(name) # 로컬변수 name 출력

def ChangeGlob(inputName): # 글로벌 변수 name을 바꿔주는 함수
    global name
    name = inputName

PrintName("World") # 이 함수 호출로 글로벌 name 변수의 값이 World로 변경 및 로컬 변수 name의 값이 Hello로 변경 후 출력
print(name) # 글로벌 변수 출력

'''
뭔가 빈약하게 코드를 짰지만 방법 1의 에러를 통해서
같은 함수 내에서 이름이 동일한 전역과 지역 변수를 구분하지는 못하는 것 같다.
그래서 방법2와 같이 전역 변수와 지역 변수 변경에 대해서 따로 따로 하는 것이 좋을 것 같다.
되도록이면 전역변수와 지역변수는 서로 다른 이름을 사용하도록 하고
같은 이름을 쓰게 되는 상황이라면 공간을 분리해서 변경할 수 있도록 해야할 것 같다.
(ex> 전역 변수만 바꿀 수 있도록 하는 함수를 선언하고 해당 함수를 다른 함수 안에서 호출하는 방법 등)
'''

# E(Enclosed function locals)영역에 대해서

def outer(): # Enclosed function locals 영역
    num = 3
    def inner(): # Local영역
        print(num) # 이것을 기준으로
    return inner

f = outer()
f()

'''
정리를 해보자면 inner 함수 안에 print(num)을 할 때 num을 찾는데
Local 영역에 없으므로 Enclosed function locals영역을 확인한다
그 영역은 Global과 local(내부함수) 사이에 있는 외부 함수 영역이고
해당 영역에 num = 3이 있으므로 결론적으로는 3을 출력한다.
'''