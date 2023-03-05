"""
    함수(Function)
        함수 선언

        def 함수명(매개변수):
            <수행문>
            return <반환값>

        def: 정의(definition)의 줄임으로 사용
        함수명: 사용자가 임의로 지정
        함수명 컨벤션(convention)
            - 짧고 명료한 이름
            - 소문자로 입력
            - 띄어쓰기는 '_'기호 사용(hello_world)
            - 동사와 명사를 함께 사용(find_name)
        매개변수(parameter): 함수에서 입력값으로 사용하는 변수
        반환값: 함수에서 반환할 결과값 지정
"""

#매개변수와 반환값이 없는 함수 - 가장 기본적인 함수
def hello_1():
    print("Hello Python")

hello_1() # 함수는 호출을 하지 않으면 실행되지 않는다.

#매개변수만 있는 함수
def hello_2(string):
    print("Hello", string)

hello_2('Python')

#반환값만 있는 함수
def hello_3():
    return "Hello python"

print(hello_3())

#매개변수와 반환 값이 있는 함수
def square(num):
    return num * num

print(square(5))

#매개변수가 여러개 있는 함수
def add(n1, n2):
    return n1 + n2

print(add(5, 8))
print(add(10, 20))

#키워드 매개변수 - 변수명을 지정해서 호출을 한다
def add(n1, n2):
    return n1 + n2

print(add(n2 = 5, n1 = 10))

#가변 매개변수 - tuple 형태로
def sum(*args):
    result = 0
    print(type(args))
    for i in args:
        result = result + i
    return result

print(sum(1, 2, 3))
print(sum(10, 30, 100))

#키워드 매개변수 - dictionary 형태로
def print_kwargs(**kwargs):
    print(type(kwargs))
    print(kwargs)

print_kwargs(n1 = 5, n2 = 8)
print_kwargs(id = 'JaeMin', pw = '1234')

#초기값 매개변수
# 매개변수에 초기값을 설정하여 사용
# 함수에 매개변수를 사용하지 않을 때 초기값을 사용
def power(b = 2, n = 2):
    return pow(b, n)
print(power())
print(power(3))
print(power(5, 2))

#여러 반환 값이 있는 함수
# 튜플 형태로 반환
def plus_and_minus(n1, n2):
    return n1 + n2, n1 - n2

result = plus_and_minus(8, 5)
print(result)

result, result2 = plus_and_minus(8, 5)
print(result, result2)


#[예제] 계산기 함수
