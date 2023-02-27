"""
    리스트(List)
        - 변경 가능한 시퀀스 자료형
        - 하나의 변수에 여러 값 할당 가능
        - 같은 자료형이 아니라 다른 자료형을 가지는 값들을 포함 가능
        - 일반적으로 비슷한 항목들의 모음을 순서대로 저장하는데 사용

    리스트 인덱싱(List Indexing)
        - 리스트의 각 위치에 해당하는 값에 접근하기 위해서 주소 개념의 숫자를 사용
        - ['One', 'Two', 'Three'] == [0] [1] [2]

    중첩 리스트 인덱싱
        - 리스트 안에 리스트가 있을 경우 인덱스 접근 방법
        - [1, 2, 3, ['One', 'Two', 'Three']]
          [0] [1] [2] [3][0] [3][1] [3][2]

    리스트 슬라이싱
        - 리스트의 인덱스를 통해서 부분만 가져올 때 사용

    중첩 리스트 슬라이싱(Nested List Slicing)
        - 중첩된 리스트에서 일부분만 인덱스를 통해서 가져올 때 사용

    리스트 연산자 / 함수 (List Operators/Function)
        - 더하기 + 연산자
        - 곱하기 * 연산자
        - 리스트 길이를 구하는 len() 함수

    리스트 수정(List Modify)
        - 리스트 인덱스 주소를 이용한 값 수정

    리스트 메소드(List Methods)
    append()
        - 리스트 요소 추가
    sort()
        - 리스트 정렬
    reverse()
        - 리스트 요소 반전
    index()
        - 리스트 요소 값에 대한 인덱스를 반환
    insert()
        - 리스트 요소 삽입
    remove()
        -리스트 요소 제거
    del()
        - 리스트 요소 제거 연산
    pop()
        - 리스트 요소 방출
    count()
        - 리스트 요소의 갯수 계산
    extend()
        - 리스트 확장


"""

#리스트(List)
print([])
print([1, 2, 3])
print(['One', 'Two', 'Three'])
print([1, 'One', 2, 'Two', 3, 'Three'])
print([1, 2, 3, ['One', 'Two', 'Three']])

#리스트 인덱싱(list indexing)
list = ['One', 'Two', 'Three']
print(list)
print(list[0])
print(list[1])
print(list[2])
print(list[-1])
print(list[-2])
print(list[-3])

#중첩 리스트 인덱싱(Nested List Indexing)
list = [1, 2, 3, ['One', 'Two', 'Three']]
print(list)
print(list[3])
print(list[3][0])
print(list[3][1])
print(list[3][2])
print('\n')

#리스트 슬라이싱(List Slicing)
list = ['One', 'Two', 'Three']
print(list)
print(list[0:])
print(list[1:2])
print(list[1:])

#중첩 리스트 슬라이싱(Nested List Slicing)
list = [1, 2, 3, ['One', 'Two', 'Three']]
print(list)
print(list[2:4])
print(list[3][2:])
print(list[3][:2])

#리스트 연산자 / 함수(List Operators/Function
list_1 = ['One', 'Two', 'Three']
list_2 = ['Four', 'Five', 'Six']
print(list_1)
print(list_2)
print(list_1 + list_2)
print(list_1 * 3)
print(len(list_1))
print(len(list_1 * 3))

#리스트 수정(List Modify)
list = ['One', 'Two', 'Three']
print(list)
list[2] = 3
print(list)
list[1] = 2
print(list)
list[0] = 1
print(list)

#리스트 메소드(List Methods)_append()
list = ['One', 'Two', 'Three']
list.append('Four')
print(list)
list.append([1, 2, 3, 4])
print(list)

#리스트 메소드(List Methods)_sort()
list = ([10, 40, 20, 30])
print(list)
list.sort()
print(list)
list = ['orange', 'apple', 'banana', 'strawberry']
print(list)
list.sort()
print(list)

#리스트 메소드(List Methods)_reverse()
list = ['orange', 'apple', 'banana', 'strawberry']
print(list)
list.reverse()
print(list)

#리스트 메소드(List Methods)_index()
list = [10, 40, 20, 30]
print(list)
print(list.index(10))
print(list.index(20))

#리스트 메소드(List Methods)_insert()
list = [10, 40, 20, 30]
print(list)
list.insert(4, 50)
print(list)
list.insert(0, 60)
print(list)

#리스트 메소드(List Methods)_remove()
list = [10, 40, 20, 30]
print(list)
list.remove(40)
print(list)
list.remove(30)
print(list)

#리스트 메소드(List Methods)_del()
list = [10, 40, 20, 30]
print(list)
del list[0]     # 삭제가 될때마다 인덱스 값이 땡겨짐
print(list)
del list[2]
print(list)

#리스트 메소드(List Methods)_pop()
list = [10, 40, 20, 30]
print(list)
list.pop()      # 젤 마지막 인덱스가 없어짐
print(list)
list.pop(0)     # 원하는 위치의 값을 없앨수도 있다.
print(list)

#리스트 메소드(List Methods)_count()
list = [10, 20, 20, 30, 30, 30]
print(list)
print(list.count(30))   # 30이라는 알맹이가 몇 개 있는지 반환
print(list.count(20))   # 20이라는 알맹이가 몇 개 있는지 반환

#리스트 메소드(List Methods)_extend()
list = [10, 40, 20, 30]
print(list)
list.extend([50, 60])
print(list)

print("리스트(list)에 대해", end="")
print("*************************************************************")
print("\n")
print("튜플(Tuple))에 대해")

"""
    튜플(Tuple)
        - 리스트와 유사하지만 변경 불가능한 시퀀스 자료형
        - 하나의 변수에 여러 값 할당 가능
        - '('와')'를 사용하여 표현
        
        튜플 인덱싱(Tuple Indexing)
            - 튜플의 각 위치에 해당하는 값에 접근하기 위해서 주소 개념의 숫자를 사용
            
        중첩 튜플 인덱싱(Nested Tuple Indexing)
            - 튜플 안에 튜플이 중첩되어 있을 경우, 인덱스 접근 방법
            
        튜플 슬라이싱 (Tuple Slicing)
            - 튜플의 인덱스를 통해서 부분만 가져올 때 사용
            
        중첩 튜플 슬라이싱 (Nested Tuple Slicing)
            - 중첩된 튜플에서 일부분만 인덱스를 통해서 가져올 때 사용
            
        #튜플 연산자/함수 (Tuple Operator/Function)
            - 더하기 + 연산
            - 곱하기 * 연산
            - 리스트 길이를 구하는 len() 함수
            
        

        
        
"""
#튜플(Tuple)
print(())
print((1, 2 ,3))
print(('One', 'Two', 'Three'))
print((1, 'One', 2, 'Two', 3, 'Three'))
print((1, 2, 3, ('One', 'Two', 'Three')))

#튜플 인덱싱(TUple Indexing)
tuple = ('One', 'Two', 'Three')
print(tuple)
print(tuple[0])
print(tuple[-1])

#중첩 튜플 인덱싱(Nested Tuple Indexing)
tuple = (1, 2, 3, ('One', 'Two', 'Three'))
print(tuple)
print(tuple[3])
print(tuple[3][1])

#튜플 슬라이싱(tuple Slicing)
tuple = ('One', 'Two', 'Three')
print(tuple)
print(tuple[0:])
print(tuple[1:2])
print(tuple[1:])

#중첩 튜플 슬라이싱(Nested Tuple Slicing)
tuple = (1, 2, 3, ('One', 'Two', 'Three'))
print(tuple)
print(tuple[3])
print(tuple[3][2:])
print(tuple[3][:2])

#튜플 연산자 / 함수 (Tuple Operator/Function)
tuple_1 = ('One', 'Two', 'Three')
tuple_2 = ('Four', 'Five', 'Six')
print(tuple_1)
print(tuple_2)
print(tuple_1 + tuple_2)
print(tuple_1 * 3)
print(len(tuple_1))
print(len(tuple_1 + tuple_2))

print("튜플(Tuple))에 대해", end="")
print("*************************************************************")
print("\n")
print("세트(Set) 대해")

"""
    세트(Set) - 집합(중복 X, 순서 X)
        - 데이터 중복을 허용하지 않는 구조
        - 순서가 없는 데이터 집합을 위한 구조
        - 인덱싱으로 값을 접근할 수 없음
        
    세트 연산자(Set Operator)
        - 교집합: &
        - 합집합: |
        - 차집합: -
        - 여집합: ^
    
    세트 메소드(Set Methods)
        - 교집합: intersection()
        - 합집합: union()
        - 차집합: difference()
        - 여집합: symmetric_difference()
        - 요소 추가: add()
        - 여러 요소 추가: update()
        - 요소 제거: remove()
        - 요소 제거: discard()
        - 모든 요소 제거: clear()
"""

# 세트(Set)
print({})
print({'One', 'Two', 'Three'})
print({10, 20, 30, 40})

# 세트 연산자(Set Operator)
set_1 = {10, 20, 20, 30}
set_2 = {30, 30, 40, 50}
print(set_1)    # 중복이 허락되지 않는다.
print(set_2)
print(set_1 & set_2)    # 둘 다 있는 것
print(set_1 | set_2)    # 중복은 하나로 포함하고, 두개 싹 다 반환
print(set_1 - set_2)    # 중복된것은 빼고 set_1 반
print(set_1 ^ set_2)    # 중복되는 30이 빠진 나머지 것 반환

# 세트 메소드(Set Methods)
set_1 = {10, 20, 20, 30}
set_2 = {30, 30, 40, 50}
print(set_1)    # 중복이 허락되지 않는다.
print(set_2)
print(set_1.intersection(set_2))
print(set_1.union(set_2))
print(set_1.difference(set_2))
print(set_1.symmetric_difference(set_2))

#요소 추가 : add()
set = {10, 20, 30, 40}
print(set)

#요소 추가 : add()
set.add(50)
print(set)

#여러 요소 추가 : update()
set.update([60, 70])
print(set)

#요소 제거 : remove()
set.remove(70)
set.remove(60)
print(set)

#요소 제거 : discard()
set.discard(30)
print(set)

#모든 요소 제거 : clear()
set.clear()
print(set)

print("세트(Set) 대해", end="")
print("*************************************************************")
print("\n")
print("딕셔너리(Dictionary) 대해")

"""
    딕셔너리(Dictionary)
        - 키(Key)와 값(Value)의 쌍으로 구성된 데이터
        - 순서가 없는 데이터
        - 키를 통해 값을 얻음
        - 동일한 키가 있을 경우 덮어씀
        
        딕셔너리 요소 추가/삭제
            - 딕셔너리의 해당 키 값에 값을 추가하여 요소 추가
            - del을 이용하여 요소 제거
            
        딕셔너리 메소드(Dictionary Methods)
            - keys(): 딕셔너리의 키 가져오기
            - value(): 딕셔너리의 값 가져오기
            - items(): 딕셔너리의 키와 값을 모두 가져오기
            - get(): 딕셔너리에서 키에 해당하는 값 가져오기
            - pop(): 딕셔너리에서 키에 해당하는 값 추출하기
            - clear(): 딕셔너리의 모든 요소 제거하기
"""

# 딕셔너리(Dictionary)
dic = {1: 'One', 2: 'Two', 3: 'Three'}
print(dic)
dic = {1: 'One', 2: 'Two', 3: 'Three',1: 'One', 2: 'Two', 3: 'Three'} # 동일한 값은 덮어쓴다.
print(dic)

# 딕셔너리 요소 추가/삭제
print('**** 추가 ****')
dic = {1: 'One', 2: 'Two', 3: 'Three'}
print(dic)
print(dic[2]) # 순서가 없다. 인덱스가 아니라 Value(키 값)을 반환
dic[4] = 'Four' # 4라는 키와 Four이라는 키 값을 추가
print(dic)
dic[5] = 'Five'
print(dic)
print('**** 제거 ****')
del dic[4] # 4의 키와 키 값을 제거
print(dic)

#딕셔너리 메소드(Dictionary Methods)
dic = {1: 'One', 2: 'Two', 3: 'Three'}
print(dic)
print(dic.keys())       #딕셔너리 키만 반환
print(dic.values())     #딕셔너리 키 값만 반환
print(dic.items())      #딕셔너리 키와 키 값 모두 반환
print(dic.get(2))       #딕셔너리 특정 키 값만 반환하는 것
print(dic.pop(3))       #딕셔너리 특정 키 값을 뺴내는 것 - 딕셔너리에서 사라진다.
print(dic)
dic.clear()             #딕셔너리의 모든 값을 지우는 것
print(dic)
