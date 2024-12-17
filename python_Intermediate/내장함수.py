# 내장함수 hasattr, getattr

# hasattr(객체, 이름) : 해당 객체에 2번째 인자인 이름 문자열과 동일한 이름의 요소를(속성, 메서드) 가지고 있으면 True, 없으면 False

class Test:
    def __init__(self):
        self.attr1 = "It's Attribute"
    
    def Method1(self):
        print("I'm Method1")

tester = Test() # 객체 생성

print(hasattr(tester, "Method1")) # 해당 객체에는 Method1이 있으므로 True
print(hasattr(tester, "attr1")) # 해당 객체에는 attr1이 있으므로 True
print(hasattr(tester, "testing")) # testing이라는 이름을 가지고 있지 않으므로 False

result1 = getattr(tester, "attr1")
result2 = tester.attr1

print(f"result1 : {result1}")
print(f"result2 : {result2}")
method = getattr(tester, "Method1") # 객체에 있는 메서드도 전달 가능
method() # 호출도 가능

# getattr(객체, 이름)
# getattr는 2번째 인자로 주는 이름과 동일한 속성을 찾아 그 값을 반환하거나 메서드 그 자체를 전달할 수 있는 함수
# 실제로 getattr(x, 'y')는 x.y와 동일한 값을 반환한다.
