#1020_김병준1
#함수

'''
#5.8 입력함수와 출력함수
s1, s2 = input('문자열 2개 입력하시오 >> ').split()
print(s1,s2)

#5.8.1 input()함수와 int()함수
num1, num2, num3 = input('세 정수를 입력하시오 >> ').split()
num1, num2, num3 = int(num1), int(num2), int(num3)
print(num1, num2, num3)

num1, num2, num3 = input('세 정수를 입력하시오 >> ').split(',')
num1, num2, num3 = int(num1), int(num2), int(num3)
print(num1, num2, num3)

#5.8.2 형식출력을 위한 format() 메소드
print('hello'.upper())
print('Guido Van Rossum'.split())           #구분자
print('Apple,Banana,Orange'.split(','))
print('Apple|Banana|Orange|Kiwi'.split('|'))

print('{} Python!'.format('Hello'))     #플레이스 홀더
print('{0} Python!'.format('Hello'))
print('I like {} and {}'.format('Python','Jave'))
print('I like {0} and {1}'.format('Python','Jave'))
print('I like {1} and {0}'.format('Python','Jave'))

#LAB 5-11
name = input('이름 입력 >> ')
age = input('나이 입력 >> ')
job = input('직업 입력 >> ')
home = input('사는 곳 입력 >> ')
print('이름은 {}, 나이는 {}, 직업은 {}, 사는 곳은 {}입니다.'.format(name,age,job,home))
print(f'이름은 {name}, 나이는 {age}, 직업은 {job}, 사는 곳은 {home}입니다.')
print('이름은', name, '나이는', age, '직업은', job, '사는 곳은', home,'입니다.')

#5.8.3 고급 format() 메소드
for i in range(2,15,2):
    print('{0:3d} {1:4d} {2:5d}'.format(i, i*i, i*i*i))
for i in range(2,15,2):
    print(f'{i:3d} {i*i:4d} {i*i*i:5d}')

print('소수점 세 자리로 표현한 원주율 = {0:10.3f}'.format(3.1415926))
print('{:,}'.format(1234567890))

#LAB 5-12
#1
print('_'.join('ABCD'))
#2
s = 'My favorite thing is monsters.'
print(s.replace('monsters', 'cartoons'))

#5.8.5 내장함수
print(abs(-100))
print(min(200,100,300,400))
print(max(200,100,300,400))
print(eval("100+200+300+400"))

a_str = "Hello Python!"
print(id(a_str))

print(type(123))
print(type(120.3))

print(bool(1))
print(bool(0))
print(bool(" "))
print(bool(""))
print(bool(None))

for x in range(1,51):
    if x % 5 == 0:
        print(x,end='')
    else:
        print('=',end='')
print()

for x in range(1,51):
    if x % 10 == 0:
        print('+',end='')
    else:
        print('-',end='')
print()

for x in range(1,6):
    print('-'*9,end='')
    print('+',end='')
print()

for x in range(1,51):
    if x % 10 == 5:
        print('+',end='')
    else:
        print('-',end='')
print()

num = 1
while num < 5:
    print(num)
    num = num + 1
else:
    print('종료')
print('종료합니다.')

deco = input('문자 입력 >> ')
num = int(input('출력 횟수 입력 >>'))
for i in range(num):
    print(deco,end='')
print("\n종료")

print('원하는 숫자만큼 데코문자를 출력하는 프로그램')
while True:
    deco = input('데코문자 입력 >> ')
    num = int(input('출력 횟수 입력 >>'))
    if num <= 0:
        print("출력 횟수는 0보다 큰 숫자 입력")
        continue
    for i in range(num):
        print(deco,end='')
    print()
    aws = input("계속 수행할까? y/n")
    if aws == 'n':
        break
print("\n 수행 종료")
'''

#과제
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


































