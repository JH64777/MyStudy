class Queue: # 선형 큐
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.rear = -1 # 들어오는 포인터
        self.front = -1 # 삭제할 때 (dequeue) 나갈 값 가리키는 포인터
    
    def isEmpty(self):
        return self.rear == self.front
    
    def isFull(self):
        return self.rear == self.capacity - 1

    def Enqueue(self, x):
        if not self.isFull():
            self.rear += 1
            self.array[self.rear] = x
        else:
            print("Overflow!!")
    
    def Dequeue(self):
        if not self.isEmpty():
            self.front += 1
            return self.array[self.front]
        else:
            print("Underflow!!")

    def Size(self):
        return self.rear - self.front
    
    def Display(self):
        for i in self.array:
            print(i, end=" ")

class CircularQueue: # 원형 큐
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.rear = 0
        self.front = 0

    def isEmpty(self): 
        return self.rear == self.front
    
    def isFull(self): # 원형 큐가 가득차 있는지 확인 (원형큐가 가득차 있는지 확인하기 위해서 일부러 0번 인덱스는 비워두고 1번 인덱스부터 채우게 되며 마지막까지 다 차게 된다면 원형이라서 그 다음 값이 0번 인덱스가 되므로 그것을 이용해서 꽉 찼는지 확인할 수 있음)
        return self.front == (self.rear + 1) % self.capacity

    def Enqueue(self, x):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity # 원형으로 데이터를 삽입하기 위해 쓰는 방법
            self.array[self.rear] = x
        else:
            print("Overflow")
    
    def Dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            print("Underflow")
    
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def Display(self):
        for i in range(self.front + 1, self.front + 1 + self.size()):
            print(self.array[i % self.capacity], " ", end="")

q1 = Queue(10)
