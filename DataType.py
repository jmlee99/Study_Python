# python 변수, 자료형, 연산자
"""
변수명 규칙
    -알파벳,숫자,언더바(_)로 선언가능
    -의미 있는 단어로 표기하는 것이 좋음
    -대소문자가 구분
    -특별한 의미가 있는 예약어는 사용할 수 없음
"""

name = "Jjam"
print(name)
num = 123
print(num)

abc = "abc"
abc_123 = 123
Abc_123 = 123
print(abc)
print(abc_123)
print(Abc_123)

"""
자료형(Data types)
    -파이썬에서 자료형은 유형에 따라서 논리형,수치형,문자형,구조형으로 구분
    -일반적으로 숫자와 문자, 그리고 구조에 따른 저장을 위해서 여러가지 구분된 자료형을 제공

불리언형 자료형(Boolean Type)
    -불리언은 True와 False값으로만 표현할 때 사용하는 자료형
    -예제코드에서 변수 b에 True값을 넣으면 불리언 자료형으로 결정
    -자료형을 변환하는 내장함수 type() 함수를 이용하여 자료형을 확인하면 bool로 변환된 결과를 볼 수 있음
"""
b = True
print(b)
print(type(b))

"""
정수형 자료형 (integer Type)
    * 10진수
        -10진수는 일반적인 숫자 표현을 그대로 사용
        -변수 i에 10진수로 숫자 10을 값으로 넣고, type()함수를 통해 자료형을 확인하기
        -결과는 정수형(int)자료형으로 출력

    * 2진수
        -2진수는 앞에 0b를 붙여서 표현
        -변수 b에 2진수 표현으로 0b010을 넣고, type()함수를 통해 자료형을 확인하기
    * 8진수
        -8진수는 앞에 0o를 붙여서 표현
        -변수o에 8진수 표현으로 0o130을 넣고 확인하기
    * 16진수
        -16진수는 앞에 0x를 붙여서 표현
        -변수 h에 16진수 표현으로 0xABC를 넣고 확인하기
        -16진수는 10진수와 달리 10부터 A~F까지 알파벳을 사용하여 표현
"""
# 10진수
i = 10
print(i)
print(type(i))
# 2진수
i = 0b010
print(i)
print(type(i))
# 8진수
i = 0o130
print(i)
print(type(i))
# 16진수
i = 0xABC
print(i)
print(type(i))

"""
실수형 자료형(Floating-Point Type)
    -실수형 자료형 표현은 고정소수점과 부동소수점으로 구분

    * 고정소수점(Fixed-Point)
        - 기본적으로 고정된 자리수의 소수를 사용하는 고정소수점 방식
        - 실수형 변수 f에 소수점이 포함된 12.34값을 넣고 확인하기
        - type(f)를 통해서 결과를 확인해보면 실수형(float) 자료형으로 출력
        - python에서는 소수에서 정수부가 0인 경우에는 제외해서 표현 가능
        - 코드에서 값 .123은 0.123을 의미
    * 부동소수점(Floating-Point)
        - 컴퓨터에서 소수점의 위치가 고정되지 않고 넣ㅂ은 범위의 값을 근사하여 표현하는 부동소수점 방식이 있음
        - python에서는 e 기호를 이용하여 지수에 대한 표현을 사용
        - e변수에 할당한 1234e-2하는 표현은 1234 X 10^-2를 의미하고 실제 결과 값은 12.34
        - type(e)함수를 통해 타입을 확인보해면 실수형
        - 마찬가지로 123e-3은 123 X 10^-3를 의미하여 결과는 0.123

"""
# 부동소수점
f = 12.34
print(f)
print(type(f))

f = .123
print(f)

# 고정소수점
e = 1234e-2
print(e)
print(type(e))

e = 123e-3
print(e)
print(type(e))

"""
복소수형 자료형(Complex Type)
    - 복소수(complex number)는 임의의 실수 a,b에 대해 a+bi의 꼴로 나타내는 수를 의미
    - 여기서 a는 실수, b는 허수 부분
    - i는 제곱하여 -1 이되는 수로 허수 단위라고 함
    - python 에서는 i 대신에 j로 표현
    - 1 + 23j와 같이 복소수로 표현하기
    - print() 함수를 이용해 출력한 결과 (1+23j)
    - 실수부는 c.real로 허수부는 c.imag로 출력
    - 복소수의 경우에는 type()함수로 타입을 살펴보면 결과는 'complex'
"""
# 한 번에 출력
c = 1 + 23j
print(c)
print(type(c))

# 따로 출력
c = 1 + 23j
print(c.real)
print(c.imag)
print(type(c))

"""
문자열 자료형(String Type)
    - 문자열(string)은 문자들의 집합을 의미
    - 문자열을 저장하는 변수를 문자열 변수라고 함

리스트 자료형(List Type)
    - 리스트(list)는 여러 값을 하나의 변수에 담을 수 있는 자료형
    - 대괄호 안에 여러 값을 쉼표를 구분자로 표현하여 리스트 변수 생성
    - 간단하게 리스트 생성과 출력을 위해 변수 i 안에 값을 1, 2, 3을 넣어보자
    - 자료형을 출력해보면 'list'라는 결과 값을 가지는 것을 알 수 있음

튜플 자료형(Tuple Type)
    - 튜플 자료형은 리스트 자료형과 유사하지만 생성,삭제,수정이 불가
    - 튜플은 괄호 안에 여러 값을 쉼표로 구분하여 사용
    - 변수 t 안에 값 1,2,3을 저장하고, 변수와 변수의 타입을 출력하자

"""
# 문자열 자료형
string = "Jjam"
print(string)
print(type(string))

# 리스트 자료형_복합된 자료형들도 선언 가능하다.
l = [1, "One", 2, "Two", 3, "Three"]
print(l)
print(type(l))

# 튜플형 자료형
t = (1, 2, 3)
print(t)
print(type(t))
"""
범위 자료형(Range Type)
    - 불변한 숫자 시퀀스 자료형

집합형 자료형(Set Type)
    - 집합 자료형은 중복과 순서가 없다는 특징을 가지며 집합 처리를 쉽게할 수 있음
    - 집합은 중괄호를 이용해서 값을 쉼표로 구분하여 넣음
    - 변수 s 안에 값 2,3,1을 넣고 변수 s의 값과 타입을 출력하기
    - 변경 불가능한 집합 자료형으로 fronzenset이 있음
"""
# 범위형 자료형
r = range(10)
print(r)
print(type(r))

# 집합형 자료형
s = {2, 3, 1}
print(s)
print(type(s))

fs = frozenset(s)
print(fs)
print(type(fs))

"""
딕셔너리 자료형(Dictionary Type)
    - 딕셔너리 자료형은 다른 자료형과 달리 키(key)와 값(value)를 한 쌍으로 갖는 자료형
    - 변수 d에 키와 값을 구분자 : 를 이용해서 쌍으로 묶어서 1:'One', 2:'Two' 형태로 넣어보자

바이트 시퀀스형(Byte Sequence Type)
    - 바이트 자료형은 1바이트 단위의 값을 연속적으로 저장하는 시퀀스 자료형
    - 1바이트는 8트비에 해당하며, 정수값 0 ~ 255(0x00 ~ 0xFF)사용
    - 이진 데이터로 사용되어지거나 1바이트 문자로 고정을 위해 사용
    - 유니코드가 아닌 문자열을 사용하는 것과 유사
    - 바이트 자료형의 시퀀스 형태로 bytearray 자료형 사용
    - 바이트 자료형의 메모리 값의 표현으로 memoryview 자료형 사용   
"""

# 딕셔리너 자료형
d = {1: 'One', 2: 'Two'}
print(d)
print(type(d))

# 바이트 시퀀스형
byte = b'\x00'
print(byte)
print(type(byte))
# 바이트 시퀀스형_문자열
byte = b"Hello"
print(byte)
print(type(byte))
# 바이트 시퀀스형_bytearray
ba = bytearray(byte)
print(ba)
print(type(ba))
# 바이트 시퀀스형_memoryview
mv = memoryview(ba)
print(mv)
print(type(mv))

"""
동적 타이핑(dynamic typing)
    - 변수의 메모리 공간 확보가 실행 시점에서 발생
    - C나 자바는 int data = 4와 같이 data 변수를 정수형으로 사전 선언
    - 파이썬은 data = 4 형태로 선언하여 data라는 변수의 자료형이 정수(integer)인지
      실수(float)인지를 프로그래머가 아닌 인터프리터가 판단
    - 파이썬 언어가 실행 시점에 동적으로 자료형 결정
    - 다른 언어들과 달리 파이썬은 매우 유연한 언어로, 할당받는 메모리 공간도 저장되는 값의 크기에 따라 동적으로
      다르게 할당 받을 수 있음
"""
print("변수에 대해", end="")
print("*************************************************************")
print("\n")
print("자료형 변환에 대해")

"""
자료형 변환
    bool()
        - bool()함수는 다양한 자료형을 불리언형으로 변환
        - 0이나 False값이 아닌 경우는 모두 True로 변환
    int()
        - int()함수는 다양한 자료형을 정수형으로 변환
        - 복소수형은 정수로 int() 함수를 통해 변환이 되지 않음
        - 불리언 형은 값으로 True와 False만 가지고 int()함수를 통해 정수로 변환되면 True는 1로 False는 0으로 변환
        - 정수값 10은과 2진수 0b010, 8진수 0o130, 16진수 0xABC는 모두 같은 정수형이라서 그대로 값을 유지하고, 10진수 형태로 변환되어 출력
        - 실수형을 정수형으로 변환하는 경우에는 고정소수점이든 부동소수점이든지 소수점 이하를 제외하고 변환, 예를 들어, 12.34는 12로 소수점을 제외하고 변환
        - 문자형은 기본적으로는 문자열을 10진수 변환, 예를 들어, int('10')은 기본 10진수로 문자열 '10'을 정수형 10으로 변환
        - 2진수, 8진수, 16진수 등의 다른 진수로 된 문자열일 경우에는 몇 진수에 해당되는지를 입력해주면 그에 맞추어 변환
        - int('010', 2)와 같이 문자열 '010'을 2진수라고 알려주고 변환하기 위해서 2라고 입력하고, 8진수와 16진수도 마찬가지이다. 
    float()
        - float() 함수는 자료형을 실수형으로 변환
        - 복소수형은 변환이 되지 않고, 문자열 형태의 2진수, 8진수, 16진수도 변환이 되지 않음
        - int() 함수를 사용한 결과와 유사하지만, 소수점 이하 값이 포함
        - 만약 소수점 이하 값이 없다면, 0으로 변환되고, 소수점 이하 값이 있는 실수형은 동일한 값으로 변환
    complex()
        - complex() 함수는 자료형을 복소수형으로 변환
        - 불리안형, 정수형, 실수형, 복소수형, 문자형 모두 복소수형으로 변환 가능
        - 허수가 있는 복소수형을 제외하고 다른 자료형은 허수 부분이 없어서 0j로 변환
    str()
        - str() 함수는 파이썬의 모든 자료형을 문자열을 변환
        - 자료형의 값을 그대로 문자열 형태로 변환
        - str()와 repr() 함수가 존재
        - str() 함수와 유사하게 repr() 함수가 존재
        - str() 함수는 내부적으로 __str__메소드를 호출
        - __str__의 경우에는 객체의 비공식적인 문자열 출력에 사용되며 사용자가 보기 쉬운 형태로 보여줄 때 사용
        - repr() 함수는 내부적으로 __repr__메소드를 호출
        - __repr__은 공식적인 문자열을 출력할때 사용되며, 주로 해당 객체를 인식할 수 있는 공식적인 문자열을 나타낼 때 사용 
    eval() 
        - eval() 함수는 뭄ㄴ자열에 포함된 수식을 계산하여 나온 결과를 반환
        - '1 + 2'라는 문자열에 대해서 그대로 출력하는 것과 달리 계산된 결과 값은 3을 출력
        - 그 밖에도 -,*,/와 같은 여러 수식들에 대해서도 계산 가능
    tuple()
        - tuple() 함수는 문자열, 리스트, 튜플 등의 자료형을 튜플 자료형으로 변환
        - 문자열 'JaeMin'을 문자 단위로 구분하여 튜플 자료형으로 변환
        - 리스트 자료형[1, 2, 3]이나 튜플 자료형(1, 2, 3)도 튜플 자료형으로 (1, 2, 3)으로 변환
    list()
        - list() 함순느 문자열, 리스트 튜플 등의 자료형을 리스트 자료형으로 변환
        - 문자열 'JaeMin', 리스트[1, 2, 3], 튜플(1, 2, 3)에 대해서 리스트 자료형으로 변환    
    set()
        - set()함수는 문자열,리스트,튜플,집합,딕셔너리 자료형을 집합 자료형으로 변환
        - 집합의 특성답게 요소에 대해서 순서를 고려하지 않고 변환
        - 리스트, 튜플, 집합 자료형도 집합 형태로 변환이 되며, 딕셔너리 자료형도 집합으로 변환
        - 딕셔너리 자료형은 키와 값으로 구성된 구조에서 키 값에 해당하는 것만 집합으로 변환
    frozenset()
        - frozenset() 함수는 문자열을 고정 집합 형태로 변환
        - set() 함수는 집합의 값을 추가 및 제거등이 가능
        - frozenset() 함수는 수정 불가능한 집합 자료형 
    dict()
        - dict() 함수는 딕셔너리 자료형으로 변환하는 역할
        - (키 : 값)으로 구성된 튜플의 시퀀스 형태로 값을 가짐
    chr()
        - chr() 함수는 정수를 문자로 변환
        - 컴퓨터에서는 문자를 처리하기 위해 각 문자마다 특정 정수값으로 매핑: ASCII  
        - chr() 함수는 ASCII 기준에 따라서 정수값에 해당하는 문자를 나타냄
        - 예를 들어, ASCII에서 정수 값 97은 문자 a에 매핑되어 chr(97)의 결과 값은 문자 a        
    ord()
        - ord() 함수는 chr()함수와 반대로 문자를 정수 값으로 변환
        - ASCII에 맞춰서 문자 'a'에 해당하는 정수 값인 97을 출력하기    
    bin()
        - bin() 함수는 정수를 2진수 문자열로 변환
        - 자료형을 2진수 표기인 '0b'가 붙은 형태의 문자열로 변환
        - bin() 함수로 True는 0b1로 출력하고, False는 0b0으로 출력하기
        - 10진수, 2진수, 8진수, 16진수로 변환되어 출력
    oct()
        - oct() 함수는 정수를 8진수 문자열로 변환
        - 불리언형, 정수형 등의 자료형을 8진수 표기인 '0o'가 붙은 형태의 문자열로 변환
        - oct() 함수를 이용해 True는 0o1로 출력되고, False는 0o0으로 출력하기
        - 10진수, 2진수, 8진수, 16진수 정수형도 8진수로 변환되어 출력
    hex()
        - hex() 함수는 정수를 16진수 문자열로 변환
        - 주어진 자료형을 16진수 표기인 '0x'가 붙은 16진수 형태의 문자열로 변환
        - 불리언형과 정수형 모두 16진수 표기의 문자열로 변환하기
    bytes()
        - bytes() 함수는 자료형을 바이트형으로 변환
        - 객체를 바이트 객체로 변환
    bytearray()
        - bytearray() 함수는 자료형을 변경가능한 바이트형으로 변환
    memoryview()
        - 바이트 자료형을 메모리의 이진 데이터로 변환한 자료형
"""
# bool()로 자료형 변환
print('*****bool() 변환*****')
print(bool(True))
print(bool(False))
print(bool(10))
print(bool(0b010))
print(bool(0o130))
print(bool(0xABC))
print(bool(12.34))
print(bool(1234e-2))
print(bool('10'))
print('\n')

# int()로 자료형 변환
print('*****int() 변환*****')
print(int(True))
print(int(False))
print(int(10))
print(int(0b010))
print(int(0o130))
print(int(0xABC))
print(int(12.34))
print(int(1234e-2))
print(int('10'))
print(int('010', 2))
print(int('130', 8))
print(int('010', 16))
print(int('ABC', 16))
print('\n')

# float()로 자료형 변환
print('*****float() 변환*****')
print(float(True))
print(float(False))
print(float(10))
print(float(0b010))
print(float(0o130))
print(float(0xABC))
print(float(12.34))
print(float(1234e-2))
print(float('10'))
print('\n')

# complex()-복소수형으로 자료형변환
print('*****complex()변환*****')
print(complex(True))
print(complex(False))
print(complex(10))
print(complex(0b010))
print(complex(0o130))
print(complex(0xABC))
print(complex(12.34))
print(complex(1 + 23j))
print(complex(1234e-2))
print(complex('10'))
print('\n')

# str()로 자료형 변환
print('*****str() 변환*****')
print(str(True))
print(str(False))
print(str(10))
print(str(0b010))
print(str(0o130))
print(str(0xABC))
print(str(12.34))
print(str(1 + 23j))
print(str(1234e-2))
print(str('10'))
print(str([1, 2, 3]))
print(str({2, 3, 1}))
print(str((1, 2, 3)))
print(str({1: 'ONE', 2: 'TWO', 3: 'Three'}))
print('\n')

# eval()로 자료형 변환
print('*****eval() 변환*****')
print("1 + 2")
print(eval("1 + 2"))
print(eval("10 + 20 + 30"))
print(eval("10 * 10"))
print(eval("100 / 10"))
print('\n')

# tuple()로 자료형 변환
print('*****tuple() 변환*****')
print(tuple('JaeMin'))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))
print('\n')

# list()로 자료형 변환
print('*****list() 변환*****')
print(list('JaeMin'))
print(list([1, 2, 3]))
print(list((1, 2, 3)))
print('\n')

# set()로 자료형 변환
print('*****set() 변환*****')
print(set('JaeMin'))
print(set([1, 2, 3]))
print(set((1, 2, 3)))
print(set({1, 2, 3}))
print(set({1: 'One', 2: 'Two'}))
print('\n')

# frozenset()로 자료형 변환
print('*****frozenset() 변환*****')
print(frozenset('JaeMin'))
print(frozenset([1, 2, 3]))

# dict()로 자료형 변환
print('*****dict() 변환*****')
print(dict({1: 'ONE', 2: 'Two'}))
print(dict({'ONE': 1, 'Two': 2}))
print('\n')

# chr()로 자료형 변환
print('*****chr() 변환*****')
print(chr(97))
print(chr(65))
print(chr(122))
print(chr(90))
print('\n')

# ord()로 자료형 변환
print('*****ord() 변환*****')
print(ord('a'))
print(ord('A'))
print(ord('z'))
print(ord('Z'))
print('\n')

# bin()로 자료형 변환
print('*****bin()변환*****')
print(bin(True))
print(bin(False))
print(bin(10))
print(bin(0b010))
print(bin(0o130))
print(bin(0xABC))
print('\n')

# oct()로 자료형 변환
print('*****oct()변환*****')
print(oct(True))
print(oct(False))
print(oct(10))
print(oct(0b010))
print(oct(0o130))
print(oct(0xABC))
print('\n')

# hex()로 자료형 변환
print('*****hex()변환*****')
print(hex(True))
print(hex(False))
print(hex(10))
print(hex(0b010))
print(hex(0o130))
print(hex(0xABC))
print('\n')

# bytes()로 자료형 변환
print('*****bytes()변환*****')
print(bytes(True))
print(bytes(False))
print(bytes(10))
print(bytes(b'Hello'))
print(bytes([1, 2, 3]))
print('\n')

# bytearray()로 자료형 변환
print('*****bytearray()변환*****')
ba = bytearray(b'hello')
print(ba)
ba[0] = ord('H')
print(ba)
print(type(ba))
print('\n')

ba = bytearray([1, 2, 3])
print(ba)
ba[0] = 4
print(ba)
print(type(ba))
print('\n')

# memoryview()로 자료형 변환
print('*****memoryview()*****')
ba = bytearray(b'hello')
mv = memoryview(ba)
ba[0] = 72
print(ba)
print(mv)
print(type(mv))

print("자료형 변환에 대해", end="")
print("*************************************************************")
print("\n")
print("자료형 계산에 대해")

"""
자료형 계산
    - 자료형들간의 계산이 가능하도록 몇 가지 유용한 내장 함수(Built-in Function)제공

    min()
        - 입력된 값들 중에서 가장 작은 값을 반환하는 함수

    max()
        - 입력된 값들 중에서 가장 큰 값을 반환하는 함수

    sum()
        - 값 들의 합을 반환

    divmod()
        - a를 b로 나눈 값과 나머지를 쌍으로 반환
        - (a//b, a%b)와 동일한 값

    abs()
        - x의 절대값을 반환

    pow()
        - a의 b승의 값을 반환

    len(s)
        - 시퀀스(문자열,바이트,튜플,리스트 등)의 갯수를 반환

    round()
        - 소수점 뒤를 반올림한 값을 반환

    all()
        - 모든 값이 True이거나 비어있을 때 True 반환

    any()
        - 어떤 값이 True이면 True반환, 값이 비어있을 때 False 반환

"""

print('*****min()*****')
print(min(1, 2, 3))
print(min([3, 4, 5]))
print('\n')

print('*****max()*****')
print(max(1, 2, 3))
print(max([3, 4, 5]))
print('\n')

print('*****sum()*****')
print(sum((1, 2, 3)))
print(sum([3, 4, 5]))
print('\n')

print('*****divmod()*****')
print(divmod(3, 5))
print(divmod(10, 5))
print(10 // 5, 10 % 5)
print('\n')

print('*****abs()*****')
print(abs(-4))
print(abs(5))
print(abs(-10))
print('\n')

print('*****pow()*****')
print(pow(10, 2))
print(pow(10, 4))
print('\n')

print('*****len(s)*****')
print(len('String'))
print(len((1, 2, 3)))
print(len([4, 5]))
print('\n')

print('*****round()*****')
print(round(3.14))
print(round(3.141527, 2))
print(round(0.6))
print(round(0.4))
print('\n')

print('*****all()*****')
print(all((1, 2, 3)))
print(all(()))
print(all((False, True, False)))
print(all((False, False, False)))
print('\n')

print('*****any()*****')
print(any((1, 2, 3)))
print(any(()))
print(any((False, True, False)))
print(any((False, False, False)))
print('\n')

print("자료형 계산에 대해", end="")
print("*************************************************************")
print("\n")
print("연산자에 대해")

"""
    연산자(Operators)
        - 피연산자의 계산을 위해 다양한 연산자들이 존재
        - 파이썬에서 제공하는 연산자들의 종류

    산술 연산자

    비교 연산자

    할당 연산자

    비트 연산자

    논리 연산자

    멤버 연산자

    식별 연산자
"""

print('*****산술 연산자*****')
a = 6
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)
print('\n')

print('*****비교 연산자*****')
a, b = 6, 4
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print('\n')

print('*****할당 연산자*****')
a, b = 6, 4
print(a, b)
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)
a %= b
print(a)
a **= b
print(a)
a //= b
print(a)
print('\n')

print('*****비트 연산자*****')
a, b = 6, 4
print(bin(a))
print(bin(b))
print(a & b, bin(a & b))
print(a | b, bin(a | b))
print(a ^ b, bin(a ^ b))
print(~a, bin(~a))
print(a << b, bin(a << b))
print(a >> b, bin(a >> b))
print('\n')

print('*****논리 연산자*****')
print(True and True)
print(True and False)
print(True or False)
print(not True)
print(not False)
print(not (True and False))
print('\n')

print('*****멤버 연산자*****')
a, b = 6, 4
l = [2, 4, 8]
print(a in l)
print(b in l)
print(a not in l)
print(b not in l)
print('\n')

print('*****식별 연산자*****')
a, b = 6, 4
print(a is b)
print(a is not b)
a, b = 5, 5
print(a is b)
print(a is not b)
print('\n')

print("연산자에 대해", end="")
print("*************************************************************")
print("\n")
print("연산자 우선순위에 대해")

"""
    연산자 우선순위(Operators Precedence)
        - 여러 연산자들이 사용되면 어떤 연산자들이 우선되는지를 결정하기 위해 연산자의 우선순위가 존재
        - 연산자 중에서 괄호가 가장 높은 연산 순위를 가지며, 논리 연산자가 가장 낮은 연산 순위를 가짐

     1.괄호 > 2. 지수(승수) > 3. 보수, 단향 덧셈과 뺄셈 > 
     4. 곱셈, 나눗셈, 나머지, 몫 > 5. 덧셈과 뺄셈 > 6. 좌우 비트 시프트 > 7. 비트 AND > 8. 비트 XOR, 비트 OR > 
     9. 비교 연산자 > 10. 동등 연산자 > 11. 할당 연산자 > 12. 식별 연산자 > 12. 멤버 연산자 > 13. 논리연산자
"""
