class Stack():
    def __init__(self, capacity):
        self.capacity = capacity # 초기 값
        self.array = [None] * self.capacity # 처음 지정한 공간을 미리 확보해두기 위해서 설정한 것 같음
        self.top = -1 # Push Pop할 때 사용될 위치 값
    
    def isEmpty(self): # 칸이 전부 비어있는지 확인하는 메서드
        return self.top == -1

    def isFull(self): # 칸이 꽉 차있는지 확인하는 메서드
        return self.top == self.capacity - 1

    def Push(self, x): # 값을 넣는 메서드
        if not self.isFull():
            self.top += 1
            self.array[self.top] = x
        else:
            raise OverflowError
    
    def Pop(self): # 값을 빼는 메서드
        if not self.isEmpty():
            value = self.array[self.top]
            self.array[self.top] = None
            self.top -= 1
            return value
        else:
            raise ValueError

    def Size(self): # 현재 값이 들어가 있는 수량을 반환하는 메서드
        return self.top + 1

    def Display(self): # 현재 있는 값들을 출력하는 메서드
        for i in self.array:
            print(i, end=" ")

s1 = Stack(2)
s1.Push(10)
s1.Push(20)
s1.Display()