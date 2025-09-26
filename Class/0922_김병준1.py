'''
#문제 1번
w = float(input('몸무게를 입력하시오 (단위:kg) >> '))
h = float(input('키를 입력하시오 (단위:cm) >> '))
H = h * 0.01
bmi = w / (H * H)
if bmi >= 40:
    print('고도비만')
elif bmi >= 25:
    print('비만')
elif bmi >= 20:
    print('표준')
else:
    print('표준 체중 미만')
print(f'bmi : {bmi}')

for i in range(5):
    print(f"{i} 이번주도 화이팅")
print()
for i in range(1,5):
    print(f"{i} 이번주도 화이팅")
print()
for i in range(1,5,2):
    print(f"{i} 이번주도 화이팅")
print()
for _ in range(1,5):
    print("이번주도 화이팅")

#LAB 4-1 2번
for i in range(5):
    print(i)
print()
for i in range(5):
    print(i,end=' ')

print(list(range(5)))
print(list(range(0,5)))
print(list(range(0,5,1)))
print(list(range(0,5,2)))
print(list(range(2,5)))
print(list(range(0,10,2)))  #짝수
print(list(range(1,10,2)))  #홀수
print(list(range(-2,-10,-2)))

#LAB 4-2 4번
print(list(range(0,-100,-1)))
print(list(range(-99,0)))

for i in range(5):
    print(i,end = ' ')
print()
for i in range(5):
    print(i,end = ' ')

s = 0
for i in range(0,11):
    s += i
print(s)

#팩토리얼 구하기
n = int(input('정수 입력 >> '))
p = 1
for i in range(1,n+1):
    p *= i
print(f'{n}팩토리얼 = {p}')

#LAB 4-3
#1번
s = 0
for i in range(0,100):
    s += i
print(f'1에서 100까지 정수의 합 : {s}')
#2번
s = 0
for i in range(0,100,2):
    s += i
print(f'1에서 100까지 짝수의 합 : {s}')
#3번
s = 0
for i in range(1,101,2):
    s += i
print(f'1에서 100까지 홀수의 합 : {s}')
  
for i in [1,2,3,4,5]:
    print(i,end=' ')
print()
for i in [1.1,2.2,3.3,4.4,5.5]:
    print(i,end=' ')
print()
for i in ['경','북','대','학','교']:
    print(i,end=' ')
print()

s = 0
for i in [1,2,3,4,5]:
    s += i
print(f'리스트의 합 : {s}')

n = [1,2,3,4,5]
print(f'리스트의 합 : {sum(n)}')

st = 'Hello'
print(list(st))

for i in range(2,10):
    for j in range(1,10):
        print(f'{i}*{j} = {i*j:2d}',end=' ')
    print()

for i in range(1,10):
    for j in range(2,10):
        print(f'{j}*{i} = {i*j:2d}',end=' ')
    print()

n = 7
for i in range(n):
    print(' '*i + '#')

#LAB 4-4
for i in range(6,-1,-1):
    print(' '*i + '#')

n = 5
for i in range(n):
    print(n-(i+1), end=' ')
n = 5
for i in range(n):
    print(s*i+1, end=' ')

#피라미드 출력
n = 5
for i in range(n):
    for j in range(n-(i+1)):
        print(' ',end=' ')
    for k in range(2*i+1):
        print('+',end=' ')
    print()

n = 5
for i in range(n):
    print(' '*(n-(i+1)),end=' ')
    print('+'*(2*i+1))

n = 5
for i in range(n):
    print(' '*(n-(i+1))+'+'*(2*i+1))

#소수 판별
n = int(input('수를 입력하세요 >> '))
is_prime = True
for num in range(2,n):
    if n%num == 0:
        is_prime = False
print(n,'is_prime :', is_prime)

primes = []
for n in range(2,101):
    is_prime = True
    for num in range(2,n):
        if n%num == 0:
            is_prime = False
    if is_prime:
        primes.append(n)
print(primes)

#while문
n = int(input('합계를 구할 수를 입력하세요 >> '))
s = 0
i = 1
while i <= n:
    s += i
    i += 1
print(f'1부터 {n}까지의 합은 {s}')

selected = None
while selected not in ['가위','바위','보']:
    selected = input('가위, 바위, 보 중에서 선택하세요 >> ')
print('선택한 값은 :', selected)

n = int(input('합계를 구할 양의 정수를 입력하세요 >> '))
s = 0
for i in range(1,n+1):
    s += i
print(f'1부터 {n}까지의 합은 {s}')

n = -1
while n <= 0:
    n = int(input('합계를 구할 양의 정수를 입력하세요 >> '))
s = 0
for i in range(1,n+1):
    s += i
print(f'1부터 {n}까지의 합은 {s}')

#break문
st = 'Programming'
for ch in st:
    if ch in ['a','e','i','o','u']:
        break
    print(ch)
print('The end')

#continue문
st = 'Programming'
for ch in st:
    if ch in ['a','e','i','o','u']:
        continue
    print(ch)
print('The end')

#연습문제

#4.12
n = int(input("정수 N을 입력하세요: "))
number = 1
for row in range(n):
    if row % 2 == 0:
        for _ in range(n):
            print(f"{number}\t", end="")
            number += 1
    else:
        start_num = number + n - 1
        for _ in range(n):
            print(f"{start_num}\t", end="")
            start_num -= 1
        number += n
    print()

#4.13
print('세 자리의 암스트롱 수 :',end=" ")
for i in range(100,1000):
    n1 = i // 100
    n2 = (i // 10)%10
    n3 = i % 10
    s = (n1**3) + (n2**3) +(n3**3)
    if i == s:
        print(i, end=' ')

#4.14
n = int(input("정수를 입력하세요 >> "))
if n < 100:     #두 자리 수 경우
    n1 = (n // 10)%10
    n2 = n % 10
    s =  (n2 * 10) + (n1)
    if n == s:
        print(f'{n}은(는) 거꾸로 정수입니다.')
    else:
        print(f'{n}은(는) 거꾸로 정수가 아닙니다.')
elif n < 1000:    #세 자리 수 경우
    n1 = n // 100
    n2 = (n // 10)%10
    n3 = n % 10
    s = (n3 * 100) + (n2 * 10) + (n1)
    if n == s:
        print(f'{n}은(는) 거꾸로 정수입니다.')
    else:
        print(f'{n}은(는) 거꾸로 정수가 아닙니다.')
else:
    n1 = n // 1000
    n2 = (n // 100)%10
    n3 = (n // 10)%10
    n4 = n % 10
    s = (n4 * 1000) + (n3 * 100) + (n2 * 10) + (n1)
    if n == s:
        print(f'{n}은(는) 거꾸로 정수입니다.')
    else:
        print(f'{n}은(는) 거꾸로 정수가 아닙니다.')


#4.15
fuel = 500
while True:
    n = int(input('충전 또는 사용한 연료를 +/- 기호와 함께 입력하시오 >> '))
    fuel += n
    print(f'현재 탱크양은 {fuel}입니다.')
    if fuel < 50:
        break
print('경고 : 연료가 10% 미만이니 충전하세요!')
'''


