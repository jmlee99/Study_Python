"""
    문자열(String)
        - 문자, 단어 등으로 구성된 문자들의 집합
        - 시퀀스 자료형(sequence data type)
        - 인덱스는 0부터 출발
"""
s = "String"
print(s)
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])
print(s[5])
# 파이썬은 유니코드로 한국어 지원
s = "문자열"
print(s)
print(s[0])
print(s[1])
print(s[2])
print('\n')

"""
    문자열 생성
        - 파이썬에서 문자열은 작은따옴표(') 또는 큰 따옴표(")로 표현

    따옴표가 있는 문자열 생성
        - 문자열에 작은따옴표가 있을 경우, 큰 따옴표로 둘러싸서 표현
        - 문자열에 큰 따옴표가 있을 경우, 작은따오모표로 둘러싸서 표현
        - 이스케이프 코드\를 이용하여 작은따옴표(')와 큰따옴표(")를 문자열에 포함

    이스케이프 문자(Escape Character)
        - 특수 문자
        - 문자앞에 백슬래시(\) 사용
        - 문자열에 특수 문자를 표현하는데 사용
        \   == 역슬래시
        \'  == 작은따옴표
        \"  == 큰따옴표
        \a  == 알람
        \b  == 백스페이스
        \f  == 폼 피드
        \n  == 라인피드
        \r  == 캐리지 리턴
        \t  == 수행 탭
        \v  == 수직 탭
        \ooo  == 8진수 문자
"""

# 문자열 생성
print('Hello')
print("파이썬 문자열입니다.")
print('''파이썬 문자열이다.''')
print("""파이썬은 문자열 처리가 뛰어나다.""")

# 따옴표가 있는 문자열 생성
string = "Python's built-in string classes"  # 문자열에 작은 따옴표 존재
print(string)
string = '모두가 "파이썬 문자열을 배운다"라고 말한다.'  # 문자열에 큰 따옴표 존재
print(string)

# 이스케이프 문자로 문자열 생성
string = 'Python\'s built-in string classes'  # 이스케이프 문자로 문자열 생성
print(string)
string = "모두가 \"파이썬 문자열을 배운다\"라고 말한다."
print(string)
print('\n')

# 여러 줄이 있는 문자열 생성
text = "동해물과 백두산이 마르고 닳도록\n하느님이 보우하사 우리나라 만세\n무궁화 삼천리 화려강산\n대한 사람, 대한으로 길이 보전하세."
print(text)

# 작은 따옴표 3개 또는 큰 따옴표 3개를 이용하여 여러 줄이 있는 문자열 생성
text = '''동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세.
무궁화 삼천리 화려강산
대한 사람, 대한으로 길이 보전하세.'''
print(text)
print('\n')

'''
    문자열 연산(String Operators
        문자열 더하기
            - 연산자를 사용하여 문자열 연결

        문자열 곱하기
            - 연산자를 사용하여 문자열 반복

        문자열 길이
            - 문자열 길이를 하구는 len() 함수 사용

        문자열 인덱싱(indexing)
            - 문자열은 리스트처럼 문자 하나하나가 상대적인 주소(offset)를 가짐
            - 이 주소를 사용해 할당된 값을 가져오는 인덱싱을 사용

        문자열 슬라이싱(slicing)
            -문자열의 주소를 이용하여 문자열을 조각(부분)을 추출
'''

# 문자열 더하기
s1 = "동해물과 "
s2 = "백두산이"
print(s1 + s2)

# 문자열 곱하기
s = "String "
print(s * 3)

# 문자열 길이(length)
s = "String "
print(len(s))
print(len(s * 3))

# 문자열 인덱싱(indexing)
s = "String"
print(s)
print(s[-6])
print(s[-5])
print(s[-4])
print(s[-3])
print(s[-2])
print(s[-1])

# 문자열 슬라이싱(slicing)
s = "JaeMinLab - JaeMin Computer Laboratory"
print(s)
print(s[0:9]) # 0에서 8까지
print(s[:9])
print(s[12:])
print(s[-10:])
print(s[-19:-11])
print('\n')

"""
    문자열 메소드(String Methods)
        - 파이썬은 문자열 처리를 아주 쉽게 처리할 수 있는 많은 메소드들을 제공
        - 문자열을 다루는 주요 메소드들을 표로 정리
        
        capitalize() / casefold()
            - 문자열 "string"에 대해 capitalize()를 실행하면, 첫 문자가 대문자인 "String"문자열로 변환
            - 문자열 "String"에 대해 casefold()를 실행하면, 모든 문자가 소문자인 "string"문자열로 변환
            
        count()
            - 문자열 "string string"에 포함된 문자 's'의 갯수를 반환하도록 count()를 실행
            - 문자 's'가 총 2개 존재하므로 2를 반환
            - 부분 문자열 'str'이 몇개인지 반환하는 것도 가능하고, 부분 문자열 'str'이 총 2개 존재하므로 2를 반환
            
        find() / rfind()
            - 문자열 "string string"에서 문자 's'의 해당 위치를 find()를 통해 반환
            - 문자열 "string string"에서 부분 분자열 "ing"의 해당 위치를 find()를 통해 반환
            - 문자열 "string string"에서 문자 's'를 해당 위치를 rfind()를 통해 오른쪽부터 탐색하여 가장 큰 인덱스를 반환
            - 문자열 "string string"에서 부분 문자열 "ring"를 해당 위치를 rfind()를 통해 오른쪽부터 탐색하여 가장 큰
                인덱스를 반환
            
        index() / rindex()
            - 문자열 "string string"에서 문자 's'의 해당 위치를 index()를 통해 반환
            - 문자열 "string string"에서 부분 문자열 "ing"의 해당 위치를 index()를 통해 반환
            - 문자열 "string string"에서 문자 's'를 해당 위치를 rindex()를 통해 오른쪽부터 탐색하여 가장 큰 인덱스를 반환
            - 문자열 "string string"에서 부분 문자열 "ring"를 해당 위치를 rindex()를 통해 오른쪽부터 탐색하여 가장 큰 인덱스를 반환
            - 문자열 "string string"에서 문자 'z'를 해당 위치를 rindex() 함수를 통해 오른쪽부터 탐색하지만 찾을 수 없어서 'ValueError'발생
        
        isalnum()
            - isalnum()은 문자열에 알파벳이나 숫자가 1개 이상 있으면 True 반환
            - 문자열 "string"은 알파벳으로 구성 되었으므로 True 반환
            - 문자열 "한글"은 알파벳으로 구성 되어있으므로 True 반환
            - 문자열 "!@#"은 특수기호로 구성 되어있으므로 False 반환
            - 문자열 "123"은 숫자들로 구성 되어있으므로 True 반환

        isalpha()
            - isalpha()는 문자열에 알파벳이 1개 이상 있으면 True 반환
            - 문자열 "string"은 알파벳으로 구성 되었으므로 True 반환
            - 문자열 "한글"은 알파벳으로 구성 되어있으므로 True 반환
            - 문자열 "!@#"은 특수기호로 구성 되어있으므로 False 반환
            - 문자열 "123"은 숫자들로 구성 되어있으므로 False 반환
            
        isdecimal()
            - isdecimal()는 문자열의 모든 문자가 10진수 문자이면 True 반환
            - 문자열 "123"은 모두 10진수 문자열이므로 True 반환
            - 문자열 "1.23"은 실수형 문자열이므로 False 반환
        
        isdigit()
            - isdigit()는 문자열의 모든 문자가 숫자일 때 True 반환
            - 문자열 "123"은 모든 문자가 숫자에 해당하므로 True 반환
            - 문자열 "1.23"은 문자 중 숫자에 해당안되는 . 이 존재하여 False

        isnumeric()
            - isnumeric()는 문자열의 모든 문자가 수치형일 때 True 반환
            - 문자열 "123"은 모든 문자가 숫자에 해당하므로 True 반환
            - 문자열 "1.23"은 문자 중 수치형에 해당안되는 . 이 존재하여 False
            
        isidentifier()
            - isidentifier()는 문자열이 파이썬에서 사용하는 식별자인 경우 True를 반환
            - 문자열 "123"은 식별자로 사용되지 않는 문자열이라서 False 반환
            - 문자열 "True"는 식별자로 사용되기 때문에 True 반환
            - 문자열 "print"는 식별자로 사용되기 떄문에 True 반환자
            
        isspace()
            - 문자열 " "은 문자열 내에 공백 문자가 있어서 True 반환
            - 문자열 "1"은 문자열 내에 공백 아닌 문자 가있어서 False 반환 
        
        istitle()
            - 문자열 "String"은 문자열 내에 제목과 같이 첫 글자가 대문자여서 True반환
            - 문자열 "STRING"은 모든 문자가 대문자이기 떄문에 False 반환
            
        islower()
            - 문자열 "string"은 모든 문자가 소문자여서 True 반환
            - 문자열 "String"은 첫 문자가 대문자여서 False 반환
            
        isupper()
            - 문자열 "STRING"은 모든 문자가 대문자여서 True 반환
            - 문자열 "String"은 첫 문자만 대문자여서 False 반환
        
        join()
            - 문자열 "String"에 대해서 join()으로 공백 문자 ''를 문자 사이마다 추가한 문자열 "String"을 반환
            - 문자열 "String"에 대해서 join()으로 공백 문자 '_'를 문자 사이마다 추가한 문자열 "S_t_r_i_n_g"를 반환
            - 문자열 "String"에 대해서 join()으로 공백 문자 '|'를 문자 사이마다 추가한 문자열 "S|t|r|i|n|g"을 반환
            
        center()/ljust()/rjust()
            - 문자열 "String"에 대해서 center()를 사용하여 너비 10에 해당하는 문자열 길이에 가운데 정렬한 문자열 'String'을 반환
            - 문자열 "String"에 대해서 ljust()를 사용하여 너비 10에 해당하는 문자열 길이에 왼쪽 정렬한 문자열 'String'로 반환
            - 문자열 "String"에 대해서 rjust()를 사용하여 너비 10에 해당하는 문자열 길이에 오른쪽 정렬한 문자열 ' String'로 반환
        
        lower()/upper()/title()/swapcase()
            - 문자열 "String"을 lower()를 이용하여 모든 문자가 소문자로 변환된 "string"반환
            - 문자열 "String"을 upper()를 이용하여 모든 문자가 대문자로 변환된 "STRING"반환
            - 문자열 "string"을 title()를 이용하여 첫 문자가 대문자로 변환된 "String"반환
            - 문자열 "String"을 swapcase()를 이용하여 대문자는 소문자로 변환되고 소문자는 대문자로 변환된 "sTRING" 반환
        
        strip()/lstrip()/rstrip()
            - 양쪽 공백이 포함된 문자열 "String"을 strip()를 통해 공백 제거
            - 양쪽 공백이 포함된 문자열 "String"을 lstrip()를 통해 왼쪽 공백 제거
            - 양쪽 공백이 포함된 문자열 "String"을 rstrip()를 통해 오른쪽 공백 제거
            
        partition()/ rpartition()
            - 문자열 "String"을 partition()를 이용하여 문자 't'기준으로 분할
            - 문자열 "String String"을 rpartition()를 이용하여 마지막 문자 'S'를 기준으로 분할
            
        replace()
            - 문자열 "String"을 replace()를 이용해 문자열 "Str"을 문자 'R'로 교체
            
        split()/ rsplit()/ splitlines()
            - 문자열 "1 2 3"을 split()의 기본 구문자르 이용하여 '1','2','3'으로 구분
            - 문자열 "1,2,3"을 split()으로 구분자'_'를 이용하여 '1','2','3'으로 구분
            - 문자열 "1 2 3"을 rsplit()으로 구분자 '_'를 이용하여 오른쪽부터 1번만 구분하여 '1_2','3'으로 구분
            - 문자열 "123\n123\n123\n"을 splitlines() 함수를 이용하여 라인 단위로 구분하여 '123, '123, '123 반환
        
        startwith()/ endswith()
            - 문자열 "String"에서 시작 문자가 'S'인지 startswith()를 통해 확인
            - 문자열 "String"에서 마지막 문자가 'g'인지 endswith()를 통해 확인  
            
        zfill()
            - 문자열 "123"에서 너비 8만큼으로 늘리고 비어있는 부분에 '0'이 채워진 문자열 "00000123"을 반환  
            
            
"""
# capitalize() / casefold()
s = "string"
print(s)
s = s.capitalize()
print(s)
s = s.casefold()
print(s)

#count
s = "string string"
print(s)
print(s.count('s'))
print(s.count("str"))

#find() / rfind()
s = "string string"
print(s.find('s'))      # 인덱스 값을 찾아줌
print(s.find("ing"))    # 문자열이 시작되는 인덱스 값 도출
print(s.rfind('s'))     # 오른쪽부터 탐색하여 찾음
print(s.rfind("ring"))  # 오른쪽부터 탐색하여 찾음

#index() / rindex()
s = "string string"
print(s.index('s'))
print(s.index("ing"))
print(s.rindex('s'))
print(s.rindex("ring"))
#print(s.rindex('z')) == ValueError를 발생 시킨다.

#isalnum()
print("string".isalnum())
print("한글".isalnum())
print("!@#".isalnum())
print("123".isalnum())

#isalnum()
print("string".isalpha())
print("한글".isalpha())
print("!@#".isalpha())
print("123".isalpha())

#isdecimal()
print("123".isdecimal())
print("1.23".isdecimal())

#isdigit
print("123".isdigit())
print("1.23".isdigit())     # . 이 있어서 False

#isnumeric()
print("123".isnumeric())
print("1.23".isnumeric())   # . 이 있어서 False

#isidentifier()
print("123".isidentifier())
print("True".isidentifier())    # 식별자
print("print".isidentifier())   # 식별자

#isspace()
print(" ".isspace())
print(" 1 ".isspace())    # 공백이 아닌 문자 1이 존재 False

#istitle()
print("String".istitle())
print("STRING".istitle())

#islower()
print("string".islower())
print("String".islower())

#isupper()
print("STRING".isupper())
print("String".isupper())

#join()
s = "String"
print(' '.join(s))
print('_'.join(s))
print('|'.join(s))

#center()/ljust/rjust()
print("'" + "String".center(10) + "'")
print("'" + "String".ljust(10) + "'")
print("'" + "String".rjust(10) + "'")


#lower()/ upper()/ title()/ swapcase()
print("String".lower())
print("String".upper())
print("string".title())
print("String".swapcase())

#strip()/ lstrip()/ rstrip()
print("   String   ".strip())
print("   String   ".lstrip())
print("   String   ".rstrip())

#partition()/ rpartition()
print("Stirng".partition('t'))
print("String String".rpartition('S'))

#replace()
print("String".replace("Str", 'R'))

#split()/ rsplit()/ splitlines()
print("1 2 3".split())
print("1_2_3".split('_'))
print("1_2_3".rsplit('_', 1))   # 오른쪽부터 1번만 스플릿
print("123\n123\n123\n".splitlines())

#startswith()/ endswith()
print("String".startswith('S'))     # 'S'로 시작하는지
print("String".endswith('g'))       # 'g'로 끝나는지

#zfill()
print("123".zfill(8))   # 너비를 8만큼 늘리고 나머지 부분을 0으로 채워줌


print("문자열생성, 문자열 연산, 문자열 메소드에 대해", end="")
print("*************************************************************")
print("\n")
print("문자열 서식에 대해")

"""
    문자열 서식(String Format)
        
        문자열 포맷팅(String Formatting)
            - 문자열 내에서 서식에 맞추어 특정 값을 삽입 또는 변경
            - 기호 % 뒤에 있는 값이 문자열 내의 서식에 순서대로 매핑
            
        문자열 포맷 코드(String Format Code)
            - 문자열 포맷팅에서 사용할 수 있는 다양한 포맷 코드
                    %s == 문자열(String)
                    %c == 문자(character)
                    %d == 정수(integer)
                    %f == 부동소수점(floating point)
                    %o == 8진수(octal)
                    %x == 16진수(hexadecimal)
                    %% == 문자 '%'
                    
        정렬, 공백, 소수점 포맷
            - 포맷 문자 앞에 숫자는 길이를 의미
            - -는 왼쪽 정렬을 의미
            - 소수점'.'뒤에 숫자는 소숫점 이하 개수를 의미
        
        문자열 format 메소드
            - 문자열 format()의 인덱스를 이용한 고급 포맷팅
            - 인덱스 번호에 따라 format()함수의 각 값들이 매핑
            
        f 문자열 포맷팅
            - 문자열 포맷팅을 위해 새롭게 나온 기능으로 문자열 앞에 f를 붙여서 구분
            - 변수 s와 n에 대해서 문자열에 포함된 이름으로 매핑하여 사용 가능
"""

#문자열 포맷팅(String Formatting)
print("나는 사과가 %d개 있다." % 2)
print("나는 사과가 %s개 있다." % "두")
print("나는 %s가 %d개 있다." % ("사과", 2))

#문자열 포맷 코드(String Format Code)
print("%8s" % "Hello")   # 오른쪽 정렬
print("%-8sPython" % "Hello")   # Hello 왼쪽 정렬
print("%0.4f" % 3.1415926535)
print("%8.2f" % 3.1415926535)
print("%-8.2f" % 3.1415926535)

#문자열 format 메소드
print("나는 사과가 {0}개 있다.".format(2))
print("나는 사과가 {0}개 있다.".format("두"))
print("나는 {0}가 {1}개 있다.".format("사과", 2))

#문자열 format 메소드2
    #문자열 format() 메소드의 인덱스 변수 이름을 이용한 포맷팅
    #변수 이름 s와 n을 지정하여 "사과"와 숫자 2를 매핑
print("나는 사과가 {n}개 있다.".format(n=2))
print("나는 {s}가 {n}개 있다.".format(s="사과", n=2))

#문자열 format 메소드 3
    #문자열 format() 함수의 정렬, 공백, 소수점
"""
            :8 == 길이 8
            :< == 왼쪽 정렬
            :> == 오른쪽 정렬
            :^ == 가운데 정렬
            :~ == '~'로 공백 채우기(정렬 문자 <,>,^ 앞에 넣은 문자로 공백 채우기)
            :0.2f == 소수점을 2자리까지 표현
            :8.4f == 길이 8, 소수점 4자리까지
            {{ == '{'문자 표현
            }} == '}'문자 표현
"""
print("{0:8}".format("Hello"))
print("{0:<8}".format("Hello"))
print("{0:>8}".format("Hello"))
print("{0:^8}".format("Hello"))
print("{0:~^8}".format("Hello"))
print("{0:-^8}".format("Hello"))
print("{0:0.2f}".format(3.1415926535))
print("{0:8.4f}".format(3.1415926535))
print("{{중괄호}}".format())

# f문자열 포맷팅
s = "사과"
n = 2
print(f"나는 사과가 {n}개 있다.")
print(f"나는 {s}가 {n}개 있다.")

# f문자열 포맷팅 2
    #기존의 문자열 포맷을 문자열 다음 기호 : 뒤에 표현하여 그대로 사용 가능
s = 'Hello'
print(f"{s:8}")
print(f"{s:<8}")
print(f"{s:>8}")
print(f"{s:^8}")
print(f"{s:~^8}")
print(f"{s:-^8}")
print(f"{3.1415926535:0.2f}")
print(f"{3.1415926535:8.4f}")
print(f"{{중괄호}}")