"""
제어문(Control Statement)

    조건문(Conditional Statement)
        - 조건에 따라 문장을 수행
        - 주어진 조건을 판단하고 상황에 맞는 처리가 필요할 때 사용
        - 파이썬에서 제공하는 조건문
            if
            else
            elif

        if문
            - if문은 True와 False를 판단하는 조건문
            - if 조건 뒤에는 콜론(:)
            - if 기본 문법
                if <조건>:
                    <문장>

        if - else문
            if <조건>:
                <문장_1>
            else:
                <문장_2>

        if-elif-else문

            if <조건>:
                <문장_1>
            elif <조건>:
                <문장_2>
            else:
                <문장_3>

        if-pass문
            - 조건문은 있지만 실행할 문장이 없는 경우, 오류가 발생하지 않도록 무시하고 넘어가는 기능

        if조건 연산자
            - 비교연산자 : <,>,==,!=,>=,<=
            - 논리연산자 : and,or,not
            - 멤버연산자 : in, not in
            - 식별연산자 : is, is not

        조건부 표현식(Conditional Expression)
            - 한 라인으로 조건식을 사용한 표현
"""
# if문을 이용한 미세먼지 측정
# 미세먼지 농도 : pm
# 35초과는 미세먼지 농도 나쁨
pm = 40
if pm > 35:
    print("미세먼지 농도 나쁨")
pm = 30
if pm > 35:
    print("미세먼지 농도 나쁨")     # 출력 안된다.

#if-else문을 이용
pm = 30
if pm > 35:
    print("미세먼지 농도 나쁨")
else:
    print("미세먼지 농도 좋음")

#if-elif-else문을 이용
# _미세먼지 농도: pm
# _미세먼지 농도 0~15: 좋음
# _미세먼지 농도16~35: 보통
# _미세먼지 농도36~75: 나쁨
# _미세먼지 농도76~  : 매우나쁨
pm = 40
if pm < 16 :
    print("미세먼지 농도: 좋음")
elif pm < 36:
    print("미세먼지 농도: 보통")
elif pm < 76:
    print("미세먼지 농도: 나쁨")
else:
    print("미세먼지 농도: 매우나쁨")


#중첩 if문 (if문 안에 if문)
# _미세먼지 농도: pm
# _미세먼지 농도 0~15: 좋음
# _미세먼지 농도16~35: 보통
# _미세먼지 농도36~75: 나쁨
# _미세먼지 농도76~  : 매우나쁨
pm =  80
if pm < 36:
    if pm < 16:
        print("미세먼지 농도: 좋음")
    else:
        print("미세먼지 농도: 보통")
else:
    if pm < 76:
        print("미세먼지 농도: 나쁨")
    else:
        print("미세먼지 농도: 매우나쁨")

#if-pass문
if 10 > 5:
    print(10)
else:
    pass

#if 조건 연산
if 2 > 1:
    print(2)
if 3 == 3:
    print(3)
if 1 != 2:
    print(1)

# 논리 연산자
rain = True
snow = True
sun = False
if rain and snow:
    print("진눈깨비")

if not sun:
    print("흐림")
else:
    print("맑음")

# 멤버 연산자
list = ['One', 'Two', 'Three']
if 'One' in list:
    print('One')

if 'Four' in list:
    print('Four')

if 'Four' not in list:
        print('No')

# 식별 연산자
if 'One' is 'One': # is 대신에 ==
    print('One')

if 'One' is not 'Two': # is not 대신에 !=
    print('One is not Two')

# 조건부 표현식 (Conditional Expression)
score = 75
msg = "통과" if score >= 70 else "탈락"
print(msg)

"""
[Ex] 학생종류
 - 8세미만  => 학생아님
 - 14세미만 => 초등학생
 - 17세미만 => 중학생
 - 20세미만 => 고등학생
 - 26세미만 => 대학생
 - 그 외에 학생아님
"""
age = 22
if age < 8:
    print("학생 아님")
elif age < 14:
    print('초등학생')
elif age < 17:
    print('중학생')
elif age < 20:
    print('고등학생')
elif age < 26:
    print('대학생')
else:
    print('학생 아님')

"""
[Ex] 학점 계산
    90점 이상 "A+"
    90점 이상 "A"
    85점 이상 "B+"
    80점 이상 "B"
    75점 이상 "C+"
    70점 이상 "C"
    65점 이상 "D+"
    60점 이상 "D"
    그 외 "F"
"""
score = 98
if score >= 95:
    print('A+')
elif score >= 90:
    print('A')
elif score >= 85:
    print('B+')
elif score >= 80:
    print('B')
elif score >= 75:
    print('C+')
elif score >= 70:
    print('C')
elif score >= 65:
    print('D+')
elif score >= 60:
    print('D')
else:
    print('F')

print("조건문에 대해", end="")
print("*************************************************************")
print("\n")
print("반복문에 대해")

"""
    반복문 (Repetitive Statement)
        - 문장을 반복적으로 수행
        - 정해진 동작을 반복하여 처리할 때 사용
        - 파이썬에서 제공하는 반복문 
            - while
            - for
            
        while문 
            - 어떤 조건이 만족하는 동안 문장을 수행하고 만족하지 않는 경우 수행 중단
            - while문 기본 문법

            while <조건>:
                <문장>기
                
        for문 
            - 반복 범위를 지정하여 반복 수행
            - for문 기본 문법
            
            for 변수 in 리스트, 튜플, 문자열:
                <문장>
            
            -range()
                - 범위 반복에 사용
                - range 문법
                for  변수 in range(시작값, 마지막값, 증가값): 
                    <문장>
                - 마지막값은 미만으로 표시한다 => 10까지 더하고 싶으면 11로 설정    
                - 시작값과 증가값은 생략 가능
                - 생략할 때 시작값은 0, 증가값은 1
                
            _기능
                - for문을 사용하면서 iterator 역할을 위해서 i 변수가 필요
                - for문을 이후에는 iterator 변수 i가 필요하지 않음
                - 이후에 사용되지 않을 변수에 어떤 이름을 부여하고 싶지 않을 때 _ 사용

            else문
                - 반복이 종료된 후에 한번 더 실행되는 문장
            
            break문
                - 반복문 종료
                
            continue문
                - 반복 조건문으로 이동
                
            리스트 내포(List Comprehension)
                - 리스트 안에 for 문과 if문 사용
"""
# while문 예제 : 1부터 10까지 출력하
i = 1
while i <= 10:
    print(i)
    i += 1

#while문 예제 : 1부터 10까지 더하기
i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
print(sum)
print('\n')

#for문 - 리스트 요소 반복
list = ['One', 'Two', 'Three']
for i in list:
    print(i)

#for문 - 튜플 요소 반복
tuple = ('One', 'Two', 'Three')
for i in tuple:
    print(i)
#for문 - 문자열 요소 반복
string = "JaeMin"
for i in string:
    print(i)
print('\n')

#range()문 1 ~ 100까지 더하기
sum = 0
for i in range(101):
    sum += i
print(sum)

#range()문 1부터 10까지 2씩 증가
for i in range(1, 11, 2):
    print(i)

#범위 반복 range를 이용한 구구단
for i  in range(2, 10):
    for j in range(1, 10):
        print('{0} x {1} = {2}'.format(i, j, i * j))

#_기눙
for _ in range(5):
    print("JaeMin")

#else문
i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1
else:
    print(sum)

sum = 0
for i in range(11):
    sum += i
else:
    print(sum)

#break문
i = 0
while i < 100:
    print(i)
    if i == 10:
        break
    i += 1

for i  in range(10):
    print(i)
    if i == 10:
        break
#continue문
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

#리스트 내포(List Comprehension)
list = [1, 2, 3, 4, 5]
print([i * 2 for i in list])
print([i * 2 for i in range(10) if i % 2 == 0])

#[예제]문자열을 역순으로 만들기
string = "JaeMin"
reverse = ""
for c in string:
    reverse = c + reverse
print(reverse)
print(string)

print("반복문에 대해", end="")
print("*************************************************************")
print("\n")
print("에러와 예외에 대해")

"""
    에러와 예외(Errors and Exceptions)
        - 프로그램에서는 에러가 발생
        - 에러에 대한 예외 처리가 필요
"""
# 에러 예제

#ZeroDivisionError
10 / 0         # 분모가 0 이면 뜨는 에러

#NameError

noname + 3     # 이름이 정의 되지 않음

#TypeError


'1' + 1         # Type가 맞지 않는 경우

#ValueError
int('String')   # int형을 바꾸지 못하는 Value가 있는 경우

