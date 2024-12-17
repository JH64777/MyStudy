# 딕셔너리 컴프리헨션은 딕셔너리를 생성하는 방법 중 하나

name = ["james", "John"]
scores = [200, 300]

chart = { k:v for k, v in zip(name, scores) } # for문을 사용해서 키와 값 형태로 딕셔너리 생성
print(chart)

# 사실 dict(zip(name, scores))가 더 간단하고 가독성이 좋음
# 하지만 점수를 2배로 해서 하고 싶을때는 딕셔너리 컴프리헨션이 좋은 선택일 수 있음

chart2 = { k : v*2 for k, v in zip(name, scores) }
print(chart2)

# if문을 사용해서 50점 보다 높은 점수를 갖는 항목만 추가하는 방법
n = ['a', 'b', 'c', 'd', 'e']
s = [35, 68, 80, 20, 10]

c = { k:v for k, v in zip(n, s) if v > 50 }
print(c)