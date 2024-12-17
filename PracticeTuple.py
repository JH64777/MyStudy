# python 튜플에 대한 연습

# 튜플은 불변한 순서가 있는 객체의 집합
# 값을 변경할 수 없다는 특징이 있다.
tp1 = (1, 3.14, "Hello", 20)
print(tp1)

# 순서가 있어 인덱스로 접근 가능
print(tp1[1]) # 3.14
print(len(tp1)) # tp1의 길이 값

for i in tp1:
    print(i) # tp1의 모든 요소를 순서대로 출력

# 튜플끼리 + 연산을 해서 요소들을 추가할 수 있다. (튜플끼리 합칠 수 있음)
tp2 = tp1 + (5, 6.12, "World")
print(tp2)

tp3 = (1, 3, 5) * 3 # *을 사용해서 반복하는 것 또한 할 수 있다.
print(tp3)

tp4 = (1, 2, 3, (4, 5, 6)) # 튜플 안에 튜플을 추가할 수 있다.
print(tp4)

tp5 = (100) # 튜플의 요소가 1개인 경우 튜플이 되지 않음 튜플로 하고 싶다면 (100, ) 처럼 뒤에 ,를 추가해야 함
print(type(tp5))

tp5 = (100, )
print(type(tp5))

# 튜플을 선언할 때 ()가 필수 조건은 아니다
tp6 = 1, 2, 3, 4, 5
print(type(tp6))

# 함수의 반환 값이 복수일 경우 튜플 형태로 반환
def TupleTest(a, b):
    return a, b
result = TupleTest(10, 20)
print(result)
print(type(result))

first, second = TupleTest("first Data", "Second Data") # 튜플을 통해서 한 번에 다수의 변수에 값을 할당할 수 있다.
print(first)
print(second)

first, second = second, first # 추가 변수 없이 값 변환 가능 ()괄호만 없을 뿐 튜플이다
print(first)
print(second)

tp7 = tuple([1, 2, 3, 4]) # tuple객체를 생성하는 메서드 tuple(iterable한 객체) 변환이 가능하다

print(1 in (1, 2, 3))
print('a' in ('f', 'c', 's'))
# 튜플은 in 연산자를 사용할 수 있다.