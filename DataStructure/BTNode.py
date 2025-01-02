class BTNode: # 이진 트리 클래스
    def __init__(self, data, left = None, right = None):
        self.data = data # 노드에 들어가는 값
        self.left = left # 왼쪽 노드로 가는 포인터
        self.right = right # 오른쪽 노드로 가는 포인터

    def Preorder(self, node): # CLR 방식 (전위 순회 방식)
        if node is None: # 탐색할 노드가 없다면
            return # 종료
        print(node.data, end=" ")
        self.Preorder(node.left) # 좌측 노드 제귀 호출
        self.Preorder(node.right) # 우측 노드 제귀 호출
    
    def Inorder(self, node): # LCR 방식 (중위 순회 방식)
        if node is None: # 탐색할 노드가 없다면
            return # 종료
        self.Inorder(node.left)
        print(node.data, end=" ")
        self.Inorder(node.right)
    
    def Postorder(self, node): # LRC 방식 (후위 순회 방식)
        if node is None: # 탐색할 노드가 없다면
            return # 종료
        self.Postorder(node.left)
        self.Postorder(node.right)
        print(node.data, end=" ")

    def CountNode(self, node): # 노드의 총 수 구하는 메서드
        if node is None:
            return 0
        return 1 + self.CountNode(node.left) + self.CountNode(node.right) # 현재 노드 + 왼쪽 서브트리 노드 수 + 오른쪽 서브트리 노드 수

    def CalcHeight(self, node): # 트리의 높이 구하는 메서드
        if node is None:
            return -1
        leftHeight = self.CalcHeight(node.left)
        rightHeight = self.CalcHeight(node.right)
        return 1 + max(leftHeight, rightHeight) # 왼쪽과 오른쪽 중 더 깊은(트리의 높이가 더 큰) 값 + 1

# 노드 생성
root = BTNode(1)
root.left = BTNode(2)
root.right = BTNode(3)

# 자식의 자식 노드 생성
root.left.left = BTNode(4)
root.left.right = BTNode(5)

'''
트리 구조
         1
        / \
       2   3
      / \
     4   5

'''