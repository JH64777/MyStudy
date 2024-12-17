# zip 객체는 두 개의 리스트를 서로 묶어줄 때 사용한다
name = ["james", "john"]
scores = [500, 1000]

z = zip(name, scores)
print(list(z))

# 각 리스트의 첫 번째 요소끼리, 두 번째 요소끼리, ... 묶어준다
# zip객체로 반환 되므로 우리가 아는 list나 dictionary 객체로 변환을 해줘야 한다.

for n, s in zip(name, scores):
    print(n, s)

# zip 객체를 위와 같이 for문에서도 사용할 수 있다.


# 딕셔너리 생성
dict1 = { "key1" : "value1", "key2" : "value2" }
print(dict1)

dict2 = dict(mary=50, bob=60)
print(dict2)

# alice = 100
# johnny = 200
# print(dict(alice, johnny))
# 위 주석된 코드는 작동하지 않는다

# zip과 함께 사용하여 딕셔너리 만들기
species = ["cat", "dog"]
name = ["pipi", "daeng"]

animals = dict(zip(name, species))
print(animals)

# setdefault메서드와 딕셔너리

data = {}

ret = data.setdefault('a', 0) # setdefault는 요소를 추가하고 추가한 요소의 value 값을 반환한다
print(ret, data)
ret = data.setdefault('b', 5)
print(ret, data)

ret = data.setdefault('a', 3) # 이미 키가 있다면 그냥 기존에 있는 키의 value 값을 반환함 (추가하는 동작 하지 X)
print(ret, data)

# 리스트 내부에 있는 원소 갯수
data2 = ["BTC", "BTC", "XRP", "ETH", "ETH", "ETH"]
print(data2.count("ETH")) # count메서드를 통해서 특정 값이 내부에 몇 개가 있는지 확인할 수 있다.

datadict = {}

for k in set(data2): # set로 타입을 변경한 이유는 중복되는 부분을 지우기 위해서이다
    count = data2.count(k)
    print(k, count)
    datadict.setdefault(k, count) # 위와 같이 count를 통해서 key와 value의 형태로 값을 넣을 수 있다.

print(datadict)