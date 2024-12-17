tp1 = 1, 2
tp2 = (1, 2)

print(tp1 is tp2) # (1, 2) 튜플이 생긴 것이므로 tp1 tp2는 모두 한 튜플을 바라본다.
# 이렇게 튜플 객체를 생성하는 것을 튜플 패킹이라고 한다.

e1, e2 = tp1 # (1, 2)인 튜플의 각 요소를 e1 e2가 각각 바인딩 하는 것을 튜플 언패킹이라고 한다
print(e1) # 1
print(e2) # 2
print(tp1[0] is e1)
print(id(tp1), id(tp2)) # 튜플은 불변 객체이므로 tp1과 tp2는 서로 같은 것을 바인딩 하고 있다
print(id(tp1[0]), id(e1))


scores = (1, 2, 3, 4, 5, 6, 7)
low, *middles, high = scores # 이런식으로 언패킹도 가능
# 가장 첫 번째 요소, 나머지 요소(나머지 값들을 바인딩 하겠다는 의미로 앞에 *을 붙임), 가장 마지막 요소로 언패킹 된 것
print(low)
print(middles)
print(high)

first, second, third, *others = scores # 언 패킹
# 처음 요소, 두 번째, 3번째, 나머지

print(first)
print(second)
print(third)
print(others) # 왜 리스트로 되는 것일까?

# 함수와 튜플의 관계

def ReturnValues(): # 여러 값을 반환하는 함수
    return 1, 2, 3, 4 # 함수가 여러 값을 반환할 경우 튜플로 패킹된 다음 해당 튜플을 반환 함

result = ReturnValues() # 한 변수로 반환 값을 받을 경우 반환되는 튜플 값을 바인딩함
a, b, c, d = ReturnValues() # 반환되는 수와 동일한 갯수의 변수들로 반환을 받으면 언패킹 되면서 각 변수들이 튜플에 있는 각 요소의 값을 바인딩하게 됨 

print(result, a, b, c, d) # 결과 : (1, 2, 3, 4) 1 2 3 4


def sum(a, b, c): # 매개변수 여러개 사용하는 함수
    return a + b + c

# 일반적인 경우
scores = (1, 2, 3)

print(sum(scores[0], scores[1], scores[2])) # 이렇게 사용하게 된다

# 튜플 언패킹 방식을 사용하는 경우
print(sum(*scores)) # 단 튜플 객체의 요소의 갯수와 매개변수의 갯수가 동일해야 함
# 언패킹으로 전달하려면 튜플 변수 맨 앞에 *을 추가해줘야 함
