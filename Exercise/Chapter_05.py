#함수와 입출력

#연습문제
#5.1
def my_greet():
    print("환영합니다.")
my_greet()
my_greet()

#5.2
def square(n):
    return n**0.5
print('3의 제곱근 :',square(3))
print('4의 제곱근 :',square(4))

#5.3
def max2(m,n):
    return max(m,n)
def min2(m,n):
    return min(m,n)
print('100과 200중 큰 수는 :',max2(100,200))
print('100과 200중 작은 수는 :',min2(100,200))

#5.4
def mile2km(m):
    km = m * 1.61
    return km
for i in range(1,6):
    print(f'{i} 마일 = {mile2km(i)} 킬로미터')

#5.5
def inch2cm(inch):
    cm = inch * 2.54
    return cm
for i in range(1,6):
    print(f'{i} 인치 = {inch2cm(i)} 센티미터')

#5.6
def cel2fah(cel):
    fah = (9/5) * cel + 32
    return fah
for i in range(10,51,10):
    print(f'섭씨 {i} 도 = 화씨 {cel2fah(i)} 도')

#5.7
def mean3(a,b,c):
    mean = (a+b+c) / 3
    return mean
def max3(a,b,c):
    return max(a,b,c)
def min3(a,b,c):
    return min(a,b,c)
n1,n2,n3 = input('세 수를 입력하시오 >> ').split()
n1=int(n1)
n2=int(n2)
n3=int(n3)
print(f'{n1}, {n2}, {n3}의 평균값은 {mean3(n1,n2,n3)}')
print(f'{n1}, {n2}, {n3}의 최댓값은 {max3(n1,n2,n3)}')
print(f'{n1}, {n2}, {n3}의 최솟값은 {min3(n1,n2,n3)}')

#5.8
n1,n2,n3,n4,n5,n6 = input('여섯 수를 입력하시오 >> ').split()
n1=int(n1)
n2=int(n2)
n3=int(n3)
n4=int(n4)
n5=int(n5)
n6=int(n6)
def mean3(a,b,c,d,e,f):
    mean = (a+b+c+d+e+f) / 6
    return mean
def max3(a,b,c,d,e,f):
    return max(a,b,c,d,e,f)
def min3(a,b,c,d,e,f):
    return min(a,b,c,d,e,f)
print(f'평균값은 {mean3(n1,n2,n3,n4,n5,n6)}')
print(f'최댓값은 {max3(n1,n2,n3,n4,n5,n6)}')
print(f'최솟값은 {min3(n1,n2,n3,n4,n5,n6)}')

#5.9-1
def calculate_stats():
    data = input("정수를 여러 개 입력하시오 : ")
    num = ""          # 한 자리씩 모아서 숫자를 만들 변수
    total = 0         # 합계
    count = 0         # 개수
    maximum = None    # 최댓값
    minimum = None    # 최솟값

    for ch in data + " ":   # 마지막 숫자까지 처리하기 위해 공백 추가
        if ch != " ":       # 공백이 아니면 숫자 이어 붙이기
            num += ch
        else:               # 공백 만나면 숫자 하나 완성
            if num != "":
                value = int(num)
                total += value
                count += 1

                if maximum is None or value > maximum:
                    maximum = value
                if minimum is None or value < minimum:
                    minimum = value

                num = ""   # 숫자 초기화

    avg = total / count
    print(f"평균값은 {avg:.1f}")
    print(f"최댓값은 {maximum}")
    print(f"최솟값은 {minimum}")

# 실행
calculate_stats()

#5.9-2
def calculate_stats():
    data = input("정수를 여러 개 입력하시오 : ")
    num = ""           # 한 자리씩 모을 임시 문자열
    numbers = []       # 입력받은 숫자들을 저장 (리스트 사용 최소화)
    
    for ch in data + " ":   # 마지막 숫자까지 처리 위해 공백 하나 더
        if ch != " ":
            num += ch
        else:
            if num != "":
                numbers.append(int(num))
                num = ""

    avg = sum(numbers) / len(numbers)   # 평균값
    maximum = max(numbers)              # 최댓값
    minimum = min(numbers)              # 최솟값

    print(f"평균값은 {avg:.1f}")
    print(f"최댓값은 {maximum}")
    print(f"최솟값은 {minimum}")

# 실행
calculate_stats()

#5.9-3
def mean_of_n(nums):
    return sum(nums) / len(nums)

def max_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)

def main():
    data = input("정수를 여러 개 입력하시오 : ")
    num = ""           
    numbers = []       
    
    # 문자열을 숫자로 변환
    for ch in data + " ":   
        if ch != " ":
            num += ch
        else:
            if num != "":
                numbers.append(int(num))
                num = ""

    # 함수 호출
    avg = mean_of_n(numbers)
    maximum = max_of_n(numbers)
    minimum = min_of_n(numbers)

    print(f"평균값은 {avg:.1f}")
    print(f"최댓값은 {maximum}")
    print(f"최솟값은 {minimum}")

# 실행
main()

#5.10
x1 = int(input("x1 좌표를 입력하시오 >> "))
y1 = int(input("y1 좌표를 입력하시오 >> "))
x2 = int(input("x2 좌표를 입력하시오 >> "))
y2 = int(input("y2 좌표를 입력하시오 >> "))
def distance(x1,y1,x2,y2):
    dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return dist
print(f'두 점의 거리 : {distance(x1,y1,x2,y2)}')

#5.11
x1 = int(input("x1 좌표를 입력하시오 >> "))
y1 = int(input("y1 좌표를 입력하시오 >> "))
x2 = int(input("x2 좌표를 입력하시오 >> "))
y2 = int(input("y2 좌표를 입력하시오 >> "))
def area(x1,y1,x2,y2):
    tarea = ((x2-x1)*(y2-y1))/2
    return tarea
print(f'직삼각형의 면적 : {area(x1,y1,x2,y2)}')

#5.12
w = int(input("밑변을 입력하시오 >> "))
h = int(input("높이을 입력하시오 >> "))
def cal_area(width, height):
    area = (width * height) / 2
    return area
print(f'삼각형의 면적 : {cal_area(w,h)}')

#5.13
Pi = 3.14
def cube_vol(s):
    volume = s ** 3
    return volume
def rect_vol(w,h,l):
    volume = l*w*h
    return volume
def cone_vol(r,h):
    volume = (1/3)*Pi*(r**2)*h
    return volume
def sph_vol(r):
    volume = (4/3)*Pi*(r**3)
    return volume
def cyl_vol(r,h):
    volume = Pi*(r**2)*h
    return volume
print(f'(1) 모서리의 길이가 12인 정육면체 부피 : {cube_vol(12)}')
print(f'(2) 모서리의 길이가 20인 정육면체 부피 : {cube_vol(20)}')
print(f'(3) 가로, 세로, 깊이가 각각 3,5,6인 직육면체 부피 : {rect_vol(3,5,6)}')
print(f'(4) 반지름과 높이가 각각 20,10인 원뿔 부피 : {cone_vol(20,10)}')
print(f'(5) 반지름이 15인 구 부피 : {sph_vol(15)}')
print(f'(6) 반지름과 높이가 각각 20,10인 원기둥 부피 : {cyl_vol(20,10)}')

#5.14
def sort2(num1, num2, num3):
    lst = []
    lst.append(num1)
    lst.append(num2)
    lst.append(num3)
    lst.sort()
    return lst
print('세 수를 입력하세요 >> ')
n1 = int(input())
n2 = int(input())
n3 = int(input())
sorted_list = sort2(n1,n2,n3)
result_str = ' '.join(map(str, sorted_list))
print(f'정렬된 리스트는 다음과 같습니다 : {result_str}')

#5.15
def my_sort(*nums):
    return sorted(nums)
result1 = my_sort(45, 3, 4, 56, 5)
print(f'결과 : {result1}')
result2 = my_sort(9, 8, 7, 6, 5, 4, 3)
print(f'결과 : {result2}')

#5.16
inputStr = input('쉼표로 구분된 정수를 여러 개 입력하시오 >> ')
inputlist = inputStr.split(',')
int_list = []
for i in inputlist:
    int_list.append(int(i.strip()))
print(f'입력된 정수의 리스트 : {int_list}')
int_list.sort()
result_list = ' '.join(map(str, int_list))
print(f'정렬된 정수의 리스트 : {result_list}')

#5.17
def sum_range(n1,n2):
    hap = 0
    for i in range(n1,n2+1):
        hap += i
    return hap
print(f'10에서 20까지의 정수의 합 : {sum_range(10,20)}')
print(f'40에서 100까지의 정수의 합 : {sum_range(40,100)}')

#5.18
import math
def range_lcm(start,end):
    num = range(start,end + 1)
    return math.lcm(*num)
n1 = int(input('범위의 시작 정수 : '))
n2 = int(input('범위의 마지막 정수 : '))
print(f'{n1}에서 {n2}까지의 정수들의 최소공배수는 : {range_lcm(n1,n2)}')

#5.19
def fibo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b
    return b
num = int(input('fibo(n)의 n을 입력하세요 : '))
print(f'fibo({num}) = {fibo(num)}')

#5.20
def fibo(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b
    return b
for i in range(0,16):
    print(f'fibo({i:>2}) = {fibo(i):>4}')

#5.21
def rrn(num):
    y = int(num[0:2])
    m = int(num[2:4])
    d = int(num[4:6])

    if y >= 50:
        year = f'19{y}'
    else:
        year = f'20{y:02d}'

    print(f'{year}년 {m}월 {d}일')
n = input('주민등록번호 첫 6숫자 형식 입력 : ')
rrn(n)

#5.22
import datetime
date = datetime.datetime.now()
print(date)
y,m,d = date.year, date.month, date.day
print(y,m,d)
print(f'현재 시간은 {y}년 {m}월 {d}일입니다.')
year = str(y)[-2:]
month = f'{m:02d}'
day = f'{d:02d}'
print(f'지금 태어난 아이의 주민등록번호 앞자리는 : {year}{month}{day}')
#5.23
def area_and_circumference(r):
    area = 3.14 * (r**2)
    circumference = 2*3.14*r
    print(f'넓이 : {area}, 둘레 : {circumference}')

while True:
    n = int(input('반지름을 입력하시오 >> '))
    if n >= 0:
        area_and_circumference(n)
    else:
        print('프로그램을 종료합니다.')
        break

#5.24
import re

def sort_korean_words_from_sentence(sentence):
    korean_words = re.findall(r'[가-힣]+', sentence)
    unique_words = sorted(list(set(korean_words)))
    return unique_words

input_text = input("여러 단어로 이루어진 글을 입력하세요 >> ")
sorted_word_list = sort_korean_words_from_sentence(input_text)

print(f"입력 문장: {input_text}")
print(f"추출 및 정렬된 단어: {sorted_word_list}")

#5.25

#5.26

#5.27

#5.28



## 0929과제 ##
# 4.4 ~ 4.11

#4.4
def order_menu():
    print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
    print('1) 햄버거\n2) 치킨\n3) 피자')
    n = int(input('1에서 3까지의 메뉴를 선택하세요 : '))
    while n > 3 or n == 0:
        n = int(input('1에서 3까지의 메뉴를 다시 선택하세요 : '))
    if n == 1:
        print('햄버거를 선택했습니다.')
    elif n == 2:
        print('치킨을 선택했습니다.')
    else:
        print('피자를 선택했습니다.')
order_menu()

#4.5
def order_menu2():
    print('맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.')
    print('1) 햄버거 (h 입력)\n2) 치킨 (c 입력)\n3) 피자(p 입력)')
    n = input('1에서 3까지의 메뉴를 선택하세요 : ')
    l = ['h','c','p']
    while n not in l:
        n = input('1에서 3까지의 메뉴를 다시 선택하세요 : ')
    if n == 'h':
        print('햄버거를 선택했습니다.')
    elif n == 'c':
        print('치킨을 선택했습니다.')
    else:
        print('피자를 선택했습니다.')
order_menu2()

#4.6
def print_star(n):
    for i in range(n,0,-1):
        print(' '*(i-1)+'*'*(n-(i-1)))
n = int(input('숫자를 입력하세요 >> '))
print_star(n)

#4.7
def dec_dis(n):
    a = 0
    for i in range(2,n):
        if n % i == 0:
            a = 1
    if a == 0:
        print(f'{n}은 소수입니다.')    
    else:
        print(f'{n}은 소수가 아닙니다.')
n = int(input('숫자를 입력하세요 >> '))
dec_dis(n)

#4.8
def Discrimination():
    for i in range(2,13):
        b = 0
        for j in range(2,i):
            if i % j == 0:
                b = 1
        if b == 0:
            print(f'{i} : 소수')
        else:
            print(f'{i} : 합성수')
Discrimination()

#4.9
def squ_sum(n):
    result = 0
    for i in range(1,n+1):
        result += i**2
    print(f'결과는 {result}입니다.')
n = int(input('숫자를 입력하세요 >> '))
squ_sum(n)

#4.10
def hap(n):
    result = 0
    for i in range(1,n+1):
        result += (1/i)**2
    print(f'결과는 {result}입니다.')
n = int(input('숫자를 입력하세요 >> '))
hap(n)

#4.11
def cnt_day(h,d):
    while True:
        d += 1
        h += 7
        print(f'day : {d}    달팽이의 위치 : {h}미터')
        if h > 30:
           break
        h -=5
    print(f'우물을 탈출하는 데 걸린 날은 {d}일 입니다.')
cnt_day(h = 0, d = 0)

#4.12
def print_num(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i, end=' ')
n = int(input('n을 입력하세요 >> '))
print_num(n)


















