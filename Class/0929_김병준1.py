#0929_김병준
#함수와 입출력


def print_star():
    print('**********')
print_star()
print_star()
print_star()
print_star()

def print_star():
    print('**********')
def print_plus():
    print('++++++++++')
print_star()
print_plus()
print_star()
print_plus()

#LAB 5-3 (2)
def print_star():
    print('**********')
def print_plus():
    print('++++++++++')
def print_hash():
    print('##########')
print_hash()
print_star()
print_plus()
print_plus()
print_star()
print_hash()

def print_star(n):
    for _ in range(n):
        print('**********')
print_star(4)

#LAB 5-4 (2)
def print_hash(n):
    for i in range(n):
        print(i, '##########')
print_hash(6)

def print_hello(n):
    print('Hello '* n)
print('Hello를 다섯 번 출력합니다.')
print_hello(5)

def print_sum(a,b):
    result = a + b
    print(f'{a}와 {b}의 합은 {result}입니다.')
print_sum(10,20)
print_sum(100,200)

#LAB 5-5
def print_sub(a,b):
    result = a - b
    print(f'{a}와 {b}의 합은 {result}입니다.')
def print_mult(a,b):
    result = a * b
    print(f'{a}와 {b}의 합은 {result}입니다.')
print_sub(10,20)
print_mult(10,20)

a = 1
b = 2
c = -8
r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print(f'해는 {r1} 또는 {r2}')

def print_root(a,b,c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print(f'해는 {r1} 또는 {r2}')
print_root(1,2,-8)
print_root(2,-6,-8)

#LAB 5-6 (1)
def print_root(a,b,c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print(f'해는 {r1} 또는 {r2}')
print_root(1,4,-21)
print_root(1,-6,8)

#LAB 5-6 (2)
def print_area(w, h):
    area = (w * h) / 2
    print(f'밑변 {w}, 높이 {h}인 삼각형의 면적은 : {area}')
print_area(10, 20)

def print_root(a,b,c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return r1, r2
result1, result2 = print_root(1,2,-8)
print(f'해는 {result1} 또는 {result2}')

def get_sum(a,b):
    return a + b
result = get_sum(100,200)
print(f'두 수의 합 : {result}')
print(f'두 수의 합 : {get_sum(100,200)}')

#LAB 5-7
def circle_area_circum(r):
    area = 3.14 * (r ** 2)
    circum = 2 * 3.14 * r
    return area, circum
radius = 10
a,c = circle_area_circum(radius)
print(f'반지름이 {radius}인 원의 면적은 {a}, 원의 둘레는 {c:.1f}')

#LAB 5-8
def muliples(n,m):
    tup = ()
    for i in range(1,m+1):
        tup = tup + (i*n,)
    return tup
r1, r2, r3, r4 = muliples(3,4)
print(r1, r2, r3, r4)
r1, r2, r3, r4, r5 = muliples(2,5)
print(r1, r2, r3, r4, r5)

def print_sum():
    result = a + b
    print(f'print_sum() 내부 : {a}과 {b}의 합은 {result}입니다.')
a = 10
b = 20
print_sum()
result = a + b
print(f'print_sum() 외부 : {a}과 {b}의 합은 {result}입니다.')

def print_sum():
    a = 100
    b = 200
    result = a + b
    print(f'print_sum() 내부 : {a}과 {b}의 합은 {result}입니다.')
a = 10
b = 20
print_sum()
result = a + b
print(f'print_sum() 외부 : {a}과 {b}의 합은 {result}입니다.')

def print_sum():
    global a,b
    a = 100
    b = 200
    result = a + b
    print(f'print_sum() 내부 : {a}과 {b}의 합은 {result}입니다.')
a = 10
b = 20
print_sum()
result = a + b
print(f'print_sum() 외부 : {a}과 {b}의 합은 {result}입니다.')

def div(a, b = 2):
    return a / b
print(f'div(4) = {div(4)}')
print(f'div(6.3) = {div(6,3)}')

def div(a = 1, b = 2):
    return a / b
print(f'div() = {div()}')
print(f'div(4) = {div(4)}')
print(f'div(6.3) = {div(6,3)}')

def func(shape, w = 1, h = 1, r = 1):
    if shape == 0:
        return w * h
    if shape == 1:
        return 3.14 * r **2
print(f'r_area = {func(0, w = 10, h = 2)}')
print(f'c_area = {func(1, r = 5)}')

#LAB 5-9
def print_name(honor, f_name, l_name):
    print(honor, f_name, l_name)
print_name(f_name = 'Gildong', l_name = 'Hong', honor = 'Dr.')
print_name('Gildong','Hong','Dr.')
'''

## 0929과제 ##
# 4.4 ~ 4.11
'''
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
