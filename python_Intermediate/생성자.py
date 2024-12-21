class Creator():
    def __init__(self, name): # 생성자, 객체가 생성될 때마다 자동으로 호출이 되는 인스턴스 메서드
        self.name = name
        print(f"생성자 : 객체({self.name})가 생성되었습니다.")

james = Creator("James") # 객체가 생성되면서 자동으로 생성자 메서드가 호출된다
# 그래서 생성자에는 대체로 객체의 초기 값을 설정해주는 작업이 존재한다.

# 생성자 또한 인스턴스 메서드이므로 클래스 영역에 존재하며 모든 객체가 해당 메서드를 참조할 수 있다.


class Car():
    count = 0 # 클래스 속성 (모든 객체가 해당 값을 참조 함)
    def __init__(self, name): # 생성자 (인스턴스 메서드)
        self.name = name
        Car.count += 1
        print(f"{self.name}이 제조되었습니다.")
    
    
    def ShowObjCount(self): # 객체 갯수 출력 메서드
        print(f"생성된 객체의 수 : {Car.count}")

lam = Car("람보르기니")
sports = Car("스포츠 카")
morning = Car("모닝")
morning.ShowObjCount() # 총 생성된 객체의 갯수 출력


'''
왜 메모리는 스택 영역과 힙 영역으로 나뉘게 된 것일까?
차라리 아예 힙 영역으로만 사용하면 안되는 것일까?
런타임 상황에서도 메모리를 자유롭게 늘릴 수 있고 줄일 수도 있기 때문에
더 자유롭게 메모리를 쓸 수 있지 않을까?
'''

'''
static 메서드와 인스턴스 메서드로 왜 두 개가 존재하는 걸까?
어차피 클래스 영역에 인스턴스 메서드, static 메서드가 둘 다 존재하고 객체들에게 참조가 되는데
왜 굳이 2개로 나뉘게 된걸까? 그냥 인스턴스 메서드 하나만 있어도 되지 않았을까?
'''