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