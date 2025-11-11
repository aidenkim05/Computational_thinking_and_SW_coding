## 1단원 ##
'''
#1
name = input('이름을 입력하세요 : ')
age = input('나이을 입력하세요 : ')
print(f'{name}님의 나이는 {age}살 입니다.')

#2
a = 15
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#3
x = 5
y = 10
x, y = y, x
print(f'x = {x}')
print(f'y = {y}')

#4
r = int(input('반지름의 길이를 입력하시오 >> '))
s = 3.14 * r ** 2
l = 2 * 3.14 * r
print(f'넓이 = {s}, 둘레 = {l:.2f}')

#5
s = int(input('초를 입력하세요 : '))
h = s // 3600
m = (s % 3600) // 60
t = (s % 3600) % 60
print(f'{h}시간 {m}분 {t}초')


## 2단원 ##

#1
n = int(input('정수 입력 >> '))
if n > 0:
    print('양수')
elif n < 0:
    print('음수')
else:
    print('0 이다.')

#2
n = int(input('점수 입력 >> '))
if n >= 60:
    print('합격')
else:
    print('불합격')

#3번
n1, n2 = input('정수 2개 입력 >> ').split()
n1 = int(n1)
n2 = int(n2)
if n1 > n2:
    print(n1)
elif n1 < n2:
    print(n2)
else:
    print('같음')

#4
n1, n2, n3 = input('정수 3개 입력 >> ').split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
max_n = -99999999
if n1 > max_n:
    max_n = n1
if n2 > max_n:
    max_n = n2
if n3 > max_n:
    max_n = n3
print(max_n)

#5
month = int(input('월을 입력 >> '))
if month == 4 | 6 | 9 | 11:
    print(f'{month}월 -> 30일')
elif month == 2:
    print(f'{month}월 -> 28일')
else:
    print(f'{month}월 -> 31일')


## 3단원 ##

#1
for i in range(1,6):
    if i < 5:
        print(i, end = ',')
    else:
        print(i, end = '')

#2
hap = 0
for i in range(1,11):
    hap += i
print(hap)

#3
n = int(input('정수 입력 >> '))
for i in range(2, n+1, 2):
    print(i)

#4
n = int(input('정수 입력 >> '))
hap = 0
for i in range(1, n+1):
    hap += i
    if i < n:
        print(i, end = ' + ')
    else:
        print(i)
print(hap)
       
#5
hap = 0
cnt = 0
while True:
    n = int(input('정수를 입력하세요 >> '))
    if n > 0:
        hap += n
        cnt += 1
    elif n < 0:
        break
    else:
        hap += n
print(f'입력된 양의 개수 : {cnt}')
print(f'합계 : {hap}')


## 4단원 ##

#1
def print_name(name):
    print(f'{name}님, 안녕하세요!')
name = input('이름을 입력사시오 >> ')
print_name(name)

#2
def add(a,b):
    return a + b
n1 = int(input('첫 번째 수 : '))
n2 = int(input('두 번째 수 : '))
print(f'결과 : {add(n1, n2)}')

#3
def check(n):
    if n == 0:
        print('0입니다.')
    elif n % 2 == 1:
        print('홀수입니다.')
    elif n % 2 == 0:
        print('짝수입니다.')
n = int(input('정수를 입력하세요 : '))
check(n)

#4
def max_num(a,b,c):
    max_n = -9999999
    if a > max_n:
        max_n = a
    if b > max_n:
        max_n = b
    if c > max_n:
        max_n = c
    return max_n
n1, n2, n3 = input('세 정수를 입력하세요 : ').split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
print(f'가장 큰 수는 {max_num(n1,n2,n3)}입니다.')

#5
def calc_cir(r):
    s = 3.14 * r ** 2
    l = 2 * 3.14 * r
    print(f'넓이 : {s}, 둘레 : {l:.1f}')
n = int(input('반지름을 입력하시오 >> '))
calc_cir(n)



## 5단원 ##

#1
fruits = ["apple", "banana", "cherry"]
print(fruits)

#2
nums = []
n1 = int(input('정수 1 입력 : '))
nums.append(n1)
n2 = int(input('정수 2 입력 : '))
nums.append(n2)
n3 = int(input('정수 3 입력 : '))
nums.append(n3)
print(nums)

#3
lis = [3, 1, 4, 1, 5]
hap = 0
for i in lis:
    hap += i
avg = hap / len(lis)
print(f'합계 : {hap}')
print(f'평균 : {avg}')

#4
score = []
n1 = int(input('점수 1 : '))
score.append(n1)
n2 = int(input('점수 2 : '))
score.append(n2)
n3 = int(input('점수 3 : '))
score.append(n3)
max_sco = score[0]
min_sco = score[0]
for i in score:
    if i > max_sco:
        max_sco = i
    if i < min_sco:
        min_sco = i
print("가장 높은 점수:", max_sco)
print("가장 낮은 점수:", min_sco)

#5
word_list = []
n = int(input('입력할 단어 수 : '))
for i in range(1,n+1):
    word = input(f'단어 {i} :')
    word_list.append(word)
for i in word_list:
    print(i,end = ' ')

x = [1, 2, 3, 4]
y = x
y[0] = 99
print(x[0])

#피라미드
n = int(input('정수 입력 >> '))
for i in range(1, n+1):
    print(' '* (n-i) + '*' * (2*i-1))

#역 피라미드
n = int(input('정수 입력 >> '))
for i in range(n,0,-1):
    print(' ' * (n-i) + '*' * (2*i-1))

#왼쪽 삼각형
n = int(input('정수 입력 >> '))
for i in range(1, n+1):
    for j in range(i):
        print('*', end = '')
    print()

#왼쪽 역삼각형
n = int(input('정수 입력 >> '))
for i in range(n,0,-1):
    for j in range(i):
        print('*',end='')
    print()

#오른쪽 삼각형
n = int(input('정수 입력 >> '))
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(i):
        print('*', end = '')
    print()

#오른쪽 역삼각형
n = int(input('정수 입력 >> '))
for i in range(n,0,-1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(i):
        print('*',end = '')
    print()

#피보나치 수열
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

nterms = int(input('몇 개의 피보나치수를 원하세요? '))
if nterms <= 0:
    print('오류 : 양수를 입력하세요.')
else:
    print('fibonacci 수열: ', end = '')
    for i in range(nterms):
        print(fibonacci(i),end = ' ')

#1
score=[]
n1 = int(input('1. 점수 입력 >> '))
n2 = int(input('2. 점수 입력 >> '))
n3 = int(input('3. 점수 입력 >> '))
score.append(n1)
score.append(n2)
score.append(n3)
print(f'총점 : {sum(score)}, 평균 : {(sum(score))/len(score):.2f}')

#2
num = []
for i in range(5):
    n = int(input(f'{i+1}번 정수 >> '))
    num.append(n)
even_list = []
odd_list = []
for j in range(5):
    if num[j] % 2 == 0:
        even_list.append(num[j])
    else:
        odd_list.append(num[j])
print(even_list)
print(odd_list)

#3
def star_tri(n):
    for i in range(1,n+1):
        for j in range(i):
            print('*',end='')
        print()
num = int(input('정수 입력 : '))
star_tri(num)

#4
def fibo(n):
    if n <= 1:
        return n        #피보나치 0부터 시작
    else:
        return (fibo(n-1) + fibo(n-2))
num = int(input('정수 입력 : '))
for i in range(num):
    print(fibo(i),end=' ')


def fibo(n):
    if n <= 1:
        return 1        #피보나치 1부터 시작
    else:
        return (fibo(n-1) + fibo(n-2))
num = int(input('정수 입력 : '))
for i in range(num):
    print(fibo(i),end=' ')
'''
num = []
for i in range(5):
    n = int(input(f'{i+1}번 정수 >> '))
    num.append(n)
max_n = -99999
min_n = 999999
for j in range(5):
    if num[j] > max_n:
        max_n = num[j]
    if num[j] < min_n:
        min_n = num[j]
print(max_n)
print(min_n)















