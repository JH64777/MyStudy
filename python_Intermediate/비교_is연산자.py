# 비교 연산자
a = [1, 2, 3, 4] # 리스트 a
b = [1, 2, 3, 4] # 리스트 b

print(a == b) # 해당 연산자는 값이 같은지에 대해서만 비교하는 연산자
print(a is b) # is 연산자는 메모리 상에서 동일한 주소에 할당된 객체인지 확인하는 연산자
# 쉽게 말해서 비교하는 객체가 서로 같은 주소를 바인딩 하고 있는지 확인하는 것
print(id(a)) # 2064522759360
print(id(b)) # 2064524800512
# a리스트 객체와 b 리스트 객체는 내부 값이 서로 같더라도 서로 다른 주소를 바인딩하고 있기 때문에 False가 나온다.

print(a[0] is b[0]) # True
# 하지만 a의 첫 번째 포인터와 b의 첫 번째 포인터가 가리키는 곳은 동일하므로
# 왜냐하면 메모리 상에 1이라는 값이 특정 구간에 할당이 되고
# a[0]과 b[0] 모두 1이라는 값을 갖기 때문에 새로 각각 만들 필요 없이 이미 만들어져 있는 1의 주소를 바인딩 했기 때문이다.

print(id(a[0]))
print(id(b[0]))
# 위 결과 값이 서로 동일한 것을 확인할 수 있다.

'''
결론적으로 is 연산자는 비교하는 피연산자들이 서로 같은 주소를 바인딩 하고 있는지를 확인해주는 연산자이다
'''