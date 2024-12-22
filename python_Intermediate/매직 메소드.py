class Magic:
    def __init__(self):
        print("객체 생성시 호출되는 메서드")

    def __call__(self, *args, **kwarg):
        print("'()'를 앞에 붙여서 호출할 수 있게 하며 ()를 사용해서 호출 시 해당 코드가 실행된다.")
    
test = Magic()
test()

# 위 예제와 같이 앞 뒤로 '_'문자가 두 개씩 붙는 메서드가 매직 메서드이며 각 매직 메서드마다 담당하는 역할이 있다.
