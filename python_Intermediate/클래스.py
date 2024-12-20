# 클래스 정의

class Robot: # 클래스 정의
    classVariable = 100 # 클래스 영역에서 생성되는 속성 (모든 객체가 클래스 영역에서 참조)

    def __init__(self, name):
        self.name = name # 해당 변수는 self키워드이기 때문에 객체 영역에 할당되는 것으로 생각하면 된다.
        # 클래스 영역에서 생성되어 객체들에 의해서 참조되는 속성은 static 속성이다. 다만, python에 static이 있는지 여부는 아직 모르겠다.
        print("Hello World!")
        print(f"I'm {self.name}")


james = Robot("James") # 객체 생성
james.tech1 = "drive" # 해당 속성은 생성된 객체 공간에서 생성되며 "drive"값을 tech1이라는 이름으로 바인딩 했다

print(james.classVariable) # 클래스 영역에 있는 속성 출력
'''
클래스를 정의하면
메모리 상에 정의된 클래스에 대한 공간이 할당된다.

객체를 생성하면 해당 생성된 객체에 대한 공간이 별도로 메모리에 할당된다.
그리고 = 연산자를 통해서 바인딩 된다.

위 예시로 본다면 클래스를 위한 공간이 메모리에 할당되고 Robot이라는 이름으로 바인딩 된다.
객체가 생성되는 코드가 실행이 되면 메모리 공간에 객체 영역이 할당 되고
james라는 이름으로 바인딩 된다.
'''
