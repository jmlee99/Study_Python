"""
    파이썬 입력과 출력
"""

"""
    표준 입출력(Standard input / Output)
        
        표준 입력 함수
            - input() 함수 : 콘솔 창을 통g해서 사용자 입력을 받는 표준 입력 함수
            - input() 함수 안에 입력을 받기 위한 질문을 텍스트로 넣을 수 있음
            
            
        표준 출력 함수
            - print() 함수 : 콘솔 창을 통해서 결과를 출력하는 표준 출력 함수
            - sep = 'separator': 개체가 분리하는 방법 지정, 기본값같은''
            - end = 'end': 끝에 출력할 항목 지정, 기본값은 '\n'
            - file : 쓰기 방법이 있는 객체, 기본값은 sys.stdout
            - flush :True일 경우 flush하고, False일 경우 버퍼, 기본값은 False
            
    파일 입출력(File Input / Output)
        파일 입출력 과정
            - 파일의 입출력 과정은 단계를 가짐
            - 파일을 열고, 파일을 읽거나 쓰고, 파일을 닫는 순서
            
        파일 열기 / 닫기
            - file.txt파일을 생성하고, 열고 닫기
            
        파일 모드(File Mode)
            - (생략): r과 동일한 모드
            - r : 읽기 모드
            - w : 쓰기 모드, 기존에 파일이 있으면 덮어쓰기
            - a : 쓰기 모드, 기존에 파일이 있으면 이어서 쓰기(append)
            - + : 읽기/ 쓰기 모드
            - t : 텍스트 모드(기본값), 텍스트 파일을 처리
            - b : 이진 모드, 이진 파일을 처리
             
"""

#표준 입력 함수
name = input("이름 :")
print(name)

#[예제] 섭씨 온도를 화씨 온도로 변환
celsius = float(input("섭씨 온도 :"))
fahrenheit = (celsius * 1.8) + 32
print("화씨 온도 :", fahrenheit)

#구구단 중의 하나의 단을 입력받아 계산
i = int(input("출력할 단 :"))
for j in range(1, 10):
    print("{0} x {1} = {2}".format(i, j, i * j))

#표준 출력 함수
print('Hello Python')
print('안녕 파이썬')
print(7)
print(3.14)
print([1, 2, 3])

print("Hello", "Python", sep='---')
print(1, 2, 3)
print(1, end=' ')
print(2, end=' ')
print(3)

#[예제]구구단 출력
    #print() 함수를 사용하여 각 단마다 한 줄로 출력

for i in range(2, 10):
    for j in range(1, 10):
        print('{0} x {1} = {2}'.format(i, j, i * j), end='\t')
    print( )

# 파일 열기 / 닫기
f = open("file.txt", 'w')
f = open("file.txt", 'r')
f.close()

#write()
f = open("file.txt", 'w')
f.write("Hello Python")
f.close()

# 파일 출력 하는 코드
file = open('file.txt')
while True:
    line = file.readline()
    if not line:
        break
    print(line)

file.close()

#writelines()
list = ['One\n', 'Two\n', 'Three\n']
f = open("file.txt", 'w')
f.writelines(list)
f.close()
# 파일 출력 하는 코드
file = open('file.txt')
while True:
    line = file.readline()
    if not line:
        break
    print(line)

file.close()

#표준입력 -> 파일 쓰기
text = input("입력 : ")
f = open("file.txt", 'w')
f.write(text)
f.close()
# 파일 출력 하는 코드
file = open('file.txt')
while True:
    line = file.readline()
    if not line:
        break
    print(line)
file.close()
# 여러 값 입력
text = [str(text + '\n') for text in input("여러 값 입력 : ").split()] # 값이 바뀔 때 마다 \n 추가되게 한다.
print(text) # split()메소드 확인
f = open("file.txt", 'w')
f.writelines(text)
f.close()

# 파일 출력 하는 코드
file = open('file.txt')
while True:
    line = file.readline()
    if not line:
        break
    print(line)
file.close()

#q를 입력할 때 까지 파일에 반복해서 입력
x = ""
text = ""
while x != 'q':
    x = input("반복 입력 : ")
    text += x + '\n'

f = open("file.txt", 'w')
f.writelines(text)
f.close()

# 파일 출력 하는 코드
file = open('file.txt')
while True:
    line = file.readline()
    if not line:
        break
    print(line)
file.close()

#[연습] 구구단 결과를 파일에 쓰기
f = open("file.txt", 'w')
for i in range(2, 10):
    for j in range(1, 10):
        f.write("{0} x {1} = {2}\n".format(i, j, i * j))
    else:
        f.write('\n')
f.close()

# 파일 출력 하는 코드
file = open('file.txt')
while True:
    line = file.readline()
    if not line:
        break
    print(line)
file.close()

print("\n")
print("*********텍스트 파일 출력*********")

#텍스트 파일 출력
f = open("anthem.txt", 'w')
f.write("동해물과 백두산이 마르고 닳도록\n")
f.write("하느님이 보우하사 우리나라 만세\n")
f.close()
#readline()
# - readline()을 이용하여 텍스트 파일을 라인 단위로 읽고 화면에 출력
f = open("anthem.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

#readlines()
f = open("anthem.txt", 'r')
lines = f.readlines()
print(lines)
f.close

#read() - 단순히 파일을 읽는 함수
f = open("anthem.txt", 'r')
data = f.read()
print(data)
f.close()

#tell() - 파일 포인터 위치 출력
f = open('anthem.txt', 'r')
while True:
    print(f.tell())
    line = f.readline()
    if not line: break
    print(line)
f.close()

#seek() - 파일 포인터 위치 이동
f = open('anthem.txt', 'r')
f.seek(46)
line = f.readline()
print(line)
f.seek(0)
line = f.readline()
print(line)
f.close()

#with문 - 항상 파일을 open()함수로 열고, close()함수로 닫아야 하는 일을 자동으로 처리
f = open('file.txt', 'w')
f.write("Hello Python")
f.close()

with open('file.txt', 'w') as f:
    f.write("Hello Python")

#표준 입력으로 받은 내용을 파일로 쓰기
f = open('file.txt', 'w')
line = ''
while True:
    line = input()
    if not line: break
    f.writelines(line + '\n')

f.close()
file = open('file.txt')
while True:
    line = file.readline()
    if not line:
        break
    print(line)
file.close()

"""
    텍스트 파일 vs 이진 파일
        - 텍스트 파일 : 사람이 읽을 수 있는 텍스트로 구성된 파일
        - 이진 파일 : 텍스트가 아닌 비트 단위의 파일
        - 이진 파일의 종류 : 그림, 음악, 영상, 프로그램 파일 등
"""


