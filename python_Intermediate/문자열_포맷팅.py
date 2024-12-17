# C언어 스타일 문자열 포맷팅

name = "James"
score = 90
print("%s의 점수는 %d입니다." % (name, score))

# format메서드를 이용한 방법

print("{}의 점수는 {}입니다.".format(name, score))

# f-string사용한 방법
print(f"{name}의 점수는 {score}입니다.")

# 특수한 글자 출력 방법
data = 3
fmt = "{{ {} }}".format(data) # format 메서드 사용 예시
fmt2 = f"{{ {data} }}" # f-string 사용 예시

print(fmt)
print(fmt2)

'''
생각해 볼 것
 - f-string이랑 format이나 C언어 스타일 문자열 포맷팅이나 성능상으로 차이점이 있는가?
 - 33번줄이 뭔 코드인지 알아볼 것
'''

# 자리수 채우기
a = 3
mystr = f"{a:03d}" # 0을 앞에 2자리 정도 채워주는 코드 (참고로 1로 해봤는데 들여쓰기였음)
print(mystr)

symbol = "BTCUSDT"
print(f"{symbol:10}") # ????? 이건 모르겠음

b = 3.141592
floatstr = f"{b:0.2f}" # 이런식으로 자릿수도 지정할 수 있음
print(floatstr)
print(b)