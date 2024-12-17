class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

mybook = Book("점프 투 파이썬", 30000)
print(mybook.title, mybook.price)

'''
class를 통해서 원하는 책 객체를 생성하여 이름과 가격을 지정하였다.
딕셔너리와 비교하였을 때 tuple에서는 label이란 것이 없다.
튜플의 장점과 딕셔너리의 장점을 결합한 방법이 namedtuple이라고 한다.
튜플(immutable 객체라서 데이터를 효과적으로 저장하며), 딕셔너리(label이 부여되어 있어서 어떤 것인지 구분하기 쉬우며 시간 복잡도가 1이다.)
'''

# namedtuple을 사용하여 위 1 ~ 7번째 줄까지의 코드를 구현한 방법
from collections import namedtuple

Document = namedtuple('Document', ['title', 'price'])
mybook2 = Document("AI를 활용한 스테가 분석", 26000)
print(mybook2.title, mybook2.price)

# namedtuple을 통해 생성한 객체는 튜플과 동일하게 immutable하기 때문에 클래스와 달리 값을 수정할 수 없다.
# 또한 튜플과 같이 정수값을 통해서 인덱싱 할 수 있다.

print(mybook2[0], mybook2[1])
# mybook2.price = 50000 # Attribute Error

# namedtuple unpacking
def print_book(title, price):
    print(f"함수에 의해 출력된 것 : {title}, {price}")

print_book(*mybook2)

# namedtuple도 튜플이기 때문에 함수에 여러 인자를 전달하는 등의 언패킹이 가능하다.

'''
리스트보다 딕셔너리가 더 효율적이라고 생각하는 이유가 무엇일까?
'''