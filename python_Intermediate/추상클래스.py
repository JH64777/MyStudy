from abc import *

class Car(metaclass=ABCMeta): # 추상 클래스
    @abstractmethod 
    def drive(self): # 추상 메서드
        pass

'''
추상 클래스란 메서드들의 이름은 정의되어 있으나 내부 로직은 정의되어 있지 않은 추상 메서드들을
가지고 있는 클래스로써 해당 클래스를 상속받아 자식 클래스 단에서 구체화할 수 있게끔 만들어진 클래스
즉, 공통적인 특징을 가진 하위 객체들을 유지보수 측면에서 더 쉽게 관리할 수 있게끔하기 위해 존재하는 클래스
'''

# test = Car() # 추상 클래스는 메서드 내부 로직이 정의되어있지 않고 이를 상속받는 하위 클래스단에서 정의할 것을 요구하기 때문에 해당 코드는 오류를 일으킴

class SportCar(Car):
    def drive(self): # 오버라이딩 방식으로 추상 클래스 Car에 있는 추상 메서드의 내부 로직을 정의해 줘야 함
        print("스포츠 카를 운전합니다.")

superCar = SportCar()
superCar.drive() # 추상 클래스에 있는 추상 메서드의 내부 로직을 정의해준 결과 작동됨
