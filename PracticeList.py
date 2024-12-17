# list에 대한 공부

# list 종류
li1 = [1, 2, 3, 4] # 숫자를 넣거나
li2 = [1, "Hello", 'c', 3.14] # 서로 다른 데이터 타입을 넣거나
li3 = [1, 2, [3, 4]] # 리스트를 요소로 넣을 수도 있음
li4 = list() # 비어있는 리스트를 만들 수 있음

# 인덱싱
print(li1[0]) # 1
print(li1[2]) # 3
print(li1[-1]) # 4 음수가 붙으면 거꾸로 생각하면 된다.
print(li3[2][0]) # 3 2번 인덱스는 리스트 요소이므로 해당 리스트 요소의 1번째 요소를 부르는 것이다. ([3, 4]리스트의 1번째 요소 == 3)

# 슬라이싱 == 특정 범위까지 잘라내는 것
st = "Hello World!"

print(li1[1:3]) # [2, 3] : 1번 ~ 2번 (3 - 1) 인덱스를 가져오는 것
print(li1[::2]) # [1, 3] : 0번부터 시작해서 2씩 증가하면서 가져오는 것
print(li1[:4]) # [1, 2, 3, 4] : 0 ~ 3번 (4 - 1) 인덱스를 가져오는 것
print(li1[2:]) # [3, 4] : 2번 ~ 3번 인덱스를 가져오는 것
print(st[:5]) # 'Hello' : 0번 ~ 4번째 글자까지 가져오는 것 (총 5개 글자)

# 리스트 더하기, 반복하기

ls1 = [1, 2, 3]
ls2 = [4, 5, 6]
print(ls1 + ls2) # [1, 2, 3, 4, 5, 6] 배열 반환
print(ls1 * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3] 배열 반환 1, 2, 3 3번 반복한 배열

# 길이 구하기
print(len(ls1)) # 3 : 총 3개의 요소를 가지고 있으므로 3을 반환한다 len은 딕셔너리나 튜플에서도 사용이 가능한 함수이다.

# 알아둬야 할 것으로는 숫자와 문자를 더하면 에러를 일으킨다는 것이다.
# print(ls1[0] + "Test") # 해당 값을 1Test라고 생각할 수 있지만 에러를 반환한다. (TypeError: unsupported operand type(s) for +: 'int' and 'str')
# 그래서 문자 1Test를 만드려면 str 함수를 사용해야 한다.
print(str(ls1[0]) + "Test")

# 요소 삭제 및 수정
ls1[0] = 10 # ls1의 첫 번째 요소 10으로 수정
print(ls1) # [10, 2, 3]

del ls1[0] # ls1의 0번 인덱스 요소를 제거한다.
print(ls1) # [2, 3]

class Test():
    def test(self):
        print("Hello Test")

test = Test() # 객체 생성
test.test()
del test # del 키워드로 객체도 삭제할 수 있다
# test.test() # 에러 반환 (NameError: name 'test' is not defined. Did you mean: 'Test'?)

ls3 = [1, 2, 3, 4, 5, 6, 7]
del ls3[:4] # 0 ~ 3번 인덱스까지의 요소들을(객체들) 삭제하는 것 <= 이렇게도 쓸 수 있음
print(ls3) # [5, 6, 7]

# 리스트 고유의 함수들
ls4 = [3, 6, 2, 1, 8, 9]
ls4.append(22) # 뒤에 값을 더해주는 함수
print(ls4)
ls4.sort() # 오름차순으로 정렬해주는 함수
print(ls4)
ls4.reverse() # 내림차순으로 정렬해주는 함수
print(ls4)
ls4.insert(5, 50) # 원하는 인덱스 번호에 값을 추가해주는 함수 (5번 인덱스, 즉 6번째로 되게끔 추가)
print(ls4)
print(ls4.index(3)) # 값이 3인 것을 찾고 인덱스 값을 반환
ls4.remove(6) # 값이 6인 것을 찾고 찾으면 해당 요소 제거 -> 만약 찾는 값이 없으면 에러 발생 (ValueError: list.remove(x): x not in list)
print(ls4)
# 먼저 찾은 값만 지우고 그 뒤에 동일한 값이 있을 경우 해당 값은 삭제되지 않음(한번 더 반복해야 함)
print(ls4.pop()) # 마지막 인덱스 요소를 반환하고 제거
print(ls4.count(4)) # 입력된 값이 리스트에 몇 개가 있는지 세어주는 함수 (4라는 값은 없으므로 0을 반환)
ls4.extend([100, 200]) # 배열을 추가해 주는 함수. 배열 + 배열이라고 생각하면 됨 (참고로 반복할 수 있는 데이터 타입을 넣어야 가능함) -> 리스트, 튜플 가능하며 딕셔너리는 key값만 들어가게 됨
print(ls4)

