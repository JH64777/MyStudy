# 변수 할당과 관련된 내용
import sys

a = 3 # 메모리에 3 할당되고 a가 바인딩(할당된 값을 가리키고 있다)
print(sys.getrefcount(a)) # 레퍼런스 카운트 값을 알 수 있는 함수
# 1000000029

b = 3 # 메모리에 3이 이미 할당되어 있으므로 b가 할당된 위치를 바인딩
print(sys.getrefcount(a)) # 레퍼런스 카운트가 1 증가하여 값은 1000000030

c = [1, 2, 3] # 가변 객체 리스트 선언 및 c로 바인딩
print(sys.getrefcount(c)) # 참조 횟수는 2 (이유는 c가 한 번, sys.getrefcount가 한 번 참조를 하므로)

d = [1, 2, 3] # 가변 객체 리스트 선언 및 d로 바인딩
print(sys.getrefcount(c)) # 참조 횟수는 2

# 내 생각에 리스트는 가변 객체이므로 값을 바꿀 시 특정 주소에 할당된 값을 변경하는 것이므로 c가 바인딩 하고 있는 객체와 d가 바인딩하고 있는 객체는 서로 다른 곳에 할당된 것 같음
# c만 바꾸고 싶어서 바꿨는데 d까지 바뀌면 안되니까...

'''
생각해 볼 것
왜 sys.getrefcount함수를 사용했을 때 a같은 경우 높은 수가 나왔는데
리스트 변수인 c, d는 왜 2라는 값만 나온 것인가?
sys.getrefcount함수는 모두 사용하고 있는데 왜 유독 리스트가 아닌 a는 높은 수가 나올까?
'''