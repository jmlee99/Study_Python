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

# 문자열 슬라이싱()