#변수와 연산자

#2.1
print(100, '+', 200, '=', 100+200)
print(200, '+', 300, '+', 400, '=', 200+300+400)

#2.2
weight = 30
height = 60
print(weight)
print(height)

#2.3
weight = 30
height = 60
print('사각형의 면적 :',weight*height)

#2.4
wight = 40
height = 20
print('삼각형의 면적 :',(wight*height)//2)

#2.5
a = int(input('정사작형의 밑변을 입력하시오 : '))
print('정사각형의 면적 : ', a*a)

#2.6
r = 0
for i in range(1,11):
    r += i
print('1에서 10까지의 합 :',r)

#2.7
r = 1
for i in range(1,11):
    r *= i
print('10! :',r)

#2.8
r = 1
print('a ** n = a**n')
for i in range(2,7):
    r = i**2
    print(i,'** 2 =',r)

#2.9
print('섭씨    화씨')
for i in range(0,51,10):
    f = (9/5) * i + 32
    print(i,'   ',f)

#2.10
c = int(input('섭씨 온도를 입력하세요 >> '))
f = (9/5) * c + 32
print('섭씨', c, ' 도는 화씨',f,'도 입니다.')

#2.11
f = int(input('화씨 온도를 입력하세요 >> '))
c = (5/9) * (f - 32)
print('화씨', f, ' 도는 섭씨',c,'도 입니다.')

#2.12
Pi = 3.141592
r = 11
l = 2*Pi*r
s = Pi*(r**2)
print('원의 반지름 =',r,'원의 둘레 =',l,'원의 넓이 =',s)

#2.13
r = int(input('원의 반지름을 입력하시오 >> '))
l = 2*Pi*r
s = Pi*(r**2)
Pi = 3.14
print('원의 둘레 =',l,'원의 넓이 =',s)

#2.14
def root(n):
    result = n**0.5
    return result

for i in range(2,11):
    print(i,'의 제곱근 =',root(i))

#2.15
a = int(input('밑변의 길이를 입력하시오 >> '))
b = int(input('높이의 길이를 입력하시오 >> '))
c = (a**2 + b**2)**0.5
print('빗변의 길이는 =',c)

#2.16
a = 1+2j
print(f'회전하기 전 : {a}')
b = a*(1j)
print(f'90도 회전한 후 : {b}')
c = a*((3**0.5)/2+0.5j)
print(f'30도 회전한 후 : {c}')

#2.17
for i in range(0,11):
    print(2<<i, end=' ')

#2.18
n = int(input('정수를 입력하시오 >> '))
if n%2 == 0:
    print('이 수가 짝수인가요? True')
else:
    print('이 수가 짝수인가요? False')

#2.19
n = int(input('정수를 입력하시오 >> '))
if n>0 and n<100:
    if n%2 == 0:
        print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? True')
    elif n%2 != 0:
        print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? False')
else:
    print('입력된 정수는 0에서 100의 범위 안에 있는 짝수인가요? False')

#2.20
print(bin(5))
print(bin(6))
print(f'{bin(5)} & {bin(6)} = {bin(5&6)}')
print(f'{bin(5)} | {bin(6)} = {bin(5|6)}')
print(f'{bin(5)} ^ {bin(6)} = {bin(5^6)}')

#2.21
n = int(input('정수를 입력하시오 >> '))
print(f'{n}의 2진수 값 : {bin(n)}')
print(f'{n}의 2진수 값에 대한 비트단위 부정값 : {bin(~n)}')

#2.22
a = int(input('정수 a를 입력하시오 >> '))
b = int(input('정수 b를 입력하시오 >> '))
print('a / b의 몫 :',a//b)
print('a / b의 나머지 :',a%b)

#2.23
n = int(input('세 자리 정수를 입력하시오 >> '))
print('백의 자리 :',n//100)
print('십의 자리 :',(n%100)//10)
print('일의 자리 :',n%10)

#2.24
n = int(input('세 자리 정수를 입력하시오 >> '))
print(n%10)
print((n%100)//10)
print(n//100)
