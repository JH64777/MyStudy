# 람다 함수 : 간단하게 함수를 정의할 때 사용하는 것
# 기존 함수 선언 방식

def NormalFunction(x): # 입력한 값에 5를 곱해서 반환하는 함수
    return 5 * x

result = NormalFunction(10)
print(result)

# 람다 함수 선언 방식

lambdaFunc = lambda x : 5 * x # 람다 함수 선언 및 lambdaFunc로 바인딩 (구조 -> lambda 매개변수: 반환할 값)
lambdaResult = lambdaFunc(10) # lambdaFunc가 선언한 람다 함수를 바인딩하고 있으므로 사용할 수 있음

print(lambdaResult)


'''
일반적인 함수 선언은 메모리에 함수 객체를 정의해 놓고 함수 선언 시 정한 이름으로 바인딩을 해주는 방식
람다 함수도 이와 동일하게 lambda 키워드를 통해서 함수 객체를 메모리에 정의
이후에 = 연산자를 통해서 정의된 람다 함수 객체를 바인딩 해준다
'''
