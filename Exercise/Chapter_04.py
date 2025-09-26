#반복문

#4.1
#1
for i in range(1,10):
    print("2 *",i, '=', 2*i)
#2
i = 1
while i <= 9:
    print("2 *",i, '=', 2*i)
    i+=1

#4.2
n = int(input('1에서 9까지의 수를 입력하세요 >> '))
while n >=10:
    num = int(input('1에서 9까지의 수를 다시  입력하세요 >> '))
    n = num
for i in range(1,10):
    print(n,"*",i, '=', n*i)

#4.3
#1)
for i in range(3):
    print('Python ')
    print('is ')
    print('FUN! ')
#2)
for i in range(3):
    print('Python ')
    print('is ')
print('FUN! ')
#3)
for i in range(3):
    print('Python ')
print('is ')
print('FUN! ')

#4.4
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

#4.5
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

#4.6#   다시 풀어보기
n = int(input('숫자를 입력하세요 >> '))
for i in range(n,0,-1):
    print(' '*(i-1)+'*'*(n-(i-1)))

#4.7#   다시 풀어보기
n = int(input('숫자를 입력하세요 >> '))
a = 0
for i in range(2,n):
    if n % i == 0:
        a = 1
if a == 0:
    print(f'{n}은 소수입니다.')    
else:
    print(f'{n}은 소수가 아닙니다.')

#4.8#   다시 풀어보기
for i in range(2,13):
    b = 0
    for j in range(2,i):
        if i % j == 0:
            b = 1
    if b == 0:
        print(f'{i} : 소수')
    else:
        print(f'{i} : 합성수')

#4.9
n = int(input('숫자를 입력하세요 >> '))
result = 0
for i in range(1,n+1):
    result += i**2
print(f'결과는 {result}입니다.')

#4.10
n = int(input('숫자를 입력하세요 >> '))
result = 0
for i in range(1,n+1):
    result += (1/i)**2
print(f'결과는 {result}입니다.')

#4.11
h = 0
d = 0
while True:
    d += 1
    h += 7
    print(f'day : {d}    달팽이의 위치 : {h}미터')
    if h > 30:
        break
    h -=5
print(f'우물을 탈출하는 데 걸린 날은 {d}일 입니다.')

#4.12
n = int(input('n을 입력하세요 >> '))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i, end=' ')



#4.12#  다시 풀어보기
# N 값 입력받기
n = int(input("정수 N을 입력하세요: "))

# 숫자 변수 초기화
number = 1

# 외부 반복문: 행(row) 처리
for row in range(n):
    # 홀수 번째 행 (0, 2, 4...)
    if row % 2 == 0:
        # 내부 반복문: 열(column)을 증가시키며 출력 (왼쪽 -> 오른쪽)
        for _ in range(n):
            print(f"{number}\t", end="")
            number += 1
    # 짝수 번째 행 (1, 3, 5...)
    else:
        # 짝수 행의 첫 번째 값 (가장 오른쪽 값) 계산
        start_num = number + n - 1
        # 내부 반복문: 열(column)을 감소시키며 출력 (오른쪽 -> 왼쪽)
        for _ in range(n):
            print(f"{start_num}\t", end="")
            start_num -= 1
        # 다음 행의 시작 숫자를 위해 number 업데이트
        number += n
    
    # 한 행의 출력이 끝난 후 줄바꿈
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

#4.16
print('1)덧셈 2)뺄셈 3)곱셈 4)나눗셈')
num = int(input('어떤 연산을 원하는지 번호를 입력하세요 >> '))
if num >= 5:
    print('잘못 입력하였습니다.')
for i in range(1,5):
    if num == i:
        print('연산을 원하는 숫자 두 개를 입력하세요')
        n1 = int(input())
        n2 = int(input())
        if num == 1:
            print(f'{n1} + {n2} =',n1+n2)
        elif num == 2:
            print(f'{n1} - {n2} =',n1-n2)
        elif num == 3:
            print(f'{n1} * {n2} =',n1*n2)
        elif num == 4:
            print(f'{n1} / {n2} =',n1/n2)

#4.17#      다시 풀어보기
limit = 20000
i = 1
while i <= limit:
    a = i
    # a의 진약수 합 계산
    sum_a = 0
    j = 1
    while j < a:
        if a % j == 0:
            sum_a = sum_a + j
        j = j + 1 
    b = sum_a
    # b가 a보다 크고 limit 범위 내에 있는지 확인
    if a < b and b <= limit:
        # b의 진약수 합 계산
        sum_b = 0
        k = 1
        while k < b:
            if b % k == 0:
                sum_b = sum_b + k
            k = k + 1     
        # 친화수 조건 확인
        if sum_b == a:
            print(f"{a}의 친화수 {b}")     
    i = i + 1

#4.14 다시 풀어보기
n = int(input("정수를 입력하세요 >> "))

# 숫자 뒤집기
rev = 0
temp = n
while temp > 0:
    digit = temp % 10      # 마지막 자리
    rev = rev * 10 + digit # 뒤집은 숫자 만들기
    temp //= 10            # 한 자리 줄이기

# 결과 비교
if n == rev:
    print(f"{n}은(는) 거꾸로 정수입니다.")
else:
    print(f"{n}은(는) 거꾸로 정수가 아닙니다.")

#4.14(2)
n = int(input("정수를 입력하세요 >> "))

s = str(n)          # 정수를 문자열로 변환
rev = ""            # 뒤집은 문자열 저장용

# 문자열을 뒤에서부터 꺼내서 저장
for ch in s:
    rev = ch + rev

# 결과 비교
if s == rev:
    print(f"{n}은(는) 거꾸로 정수입니다.")
else:
    print(f"{n}은(는) 거꾸로 정수가 아닙니다.")
