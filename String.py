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