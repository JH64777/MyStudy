class SList: # 단순 연결 리스트 클래스
    class Node: # 노드 클래스
        def __init__(self, data):
            self.data = data
            self.pointer = None
    
    def __init__(self): # SList의 초기 설정
        self.head = None
        self.size = 0
    
    def GetSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def GetNode(self, p): # p번째 노드 리턴
        if p < 0 or p > self.size: # 유효하지 않는 범위 혹은 현재 size보다 큰 범위를 선택할 시
            return None # 찾지 못했다는 의미의 None 값 반환
        else:
            curr = self.head
            for i in range(p):
                curr = curr.pointer
            return curr

    def getEntry(self, p): # p번째 노드가 가지고 있는 data값 반환
        node = self.GetNode(p)
        if node == None: # 만일 node를 찾지 못했다면
            return None # 실패했다는 의미의 None 값을 반환
        else:
            return node.data

    def Insert(self, data, p): # 새로운 값 삽입
        new_node = self.Node(data) # 새 노드 생성

        before = self.GetNode(p-1)
        if before == None: # 리스트에 노드가 없을 시
            new_node.pointer = self.head
            self.head = new_node
        else:
            new_node.pointer = before.pointer
            before.pointer = new_node
        self.size += 1
    
    def Delete(self, p):
        if self.isEmpty(): # 노드가 없을 시
            print("UnderFlow")
            return
        elif self.size < p: # 노드의 위치가 범위를 벗어났다면
            print("No Data")
            return
        elif p == 0: # 첫 번째 노드를 삭제하려면
            self.head = self.head.pointer
        else: # 일반적인 삭제 상황
            before = self.GetNode(p-1)
            curr = self.GetNode(p)
            before.pointer = curr.pointer
        self.size -= 1
    
    def Search(self, data): # data를 가지고 있는 Node를 찾는 메서드
        curr = self.head
        for i in range(self.size):
            if data == curr.data:
                return i
            curr = curr.pointer
        return False

    def Display(self): # 모든 노드의 data 값을 출력하는 메서드
        curr = self.head
        for i in range(self.size):
            print(curr.data, end=" -> ")
            curr = curr.pointer
        print("None")


slist = SList()
slist.Insert(13, 1)
slist.Display()