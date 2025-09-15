'''
#문제 1번
#지름이 30cm인 피자를 1/4등분하였다.
#이 조각의 넓이와 데이터의 타입을 출력하시오
#(단, 넓이는 제곱센티미터로 출력한다.)
r = 30;
Pi = 3.14
s = Pi * r**2
pizza = s/4
print(pizza,'cm^2 \n데이터 타입 :',type(pizza))

### 조건문 ###

#if문 사용법
#상황 1
age = int(input('나이를 입력하시오 >> '))
if age < 20:
    print('청소년 할인')
    
#상황 2
walk_count = int(input('걸음수를 입력하시오 >> '))
if walk_count >= 1000:
    print('목표 달성')

#LAB 3-1
#1번
game_score = int(input('game_score = '))
print(game_score)
if game_score >= 1000:
    print('당신은 고수입니다.')
    
#2번
num_a = int(input('num_a = '))
num_b = int(input('num_b = '))
if num_a == num_b:
    print('두 값은 일치합니다.')

#들여쓰기의 중요성
age = int(input('나이를 입력하시오 >> '))
if age < 20:
    print('청소년 할인')
print('입장을 환영합니다.')     

age = int(input('나이를 입력하시오 >> '))
if age < 20:
    print('청소년 할인')
    print('입장을 환영합니다.')
  
age = int(input('나이를 입력하시오 >> '))
if age < 20:
print('청소년 할인')         #오류
print('입장을 환영합니다.')

#LAB 3-2
#1
n = int(input('정수를 입력하세요 : '))
print('n =',n)
if n % 2 == 0:
    print(n,'은(는) 짝수입니다.')

#LAB 3-3
#2
n = int(input('당신은 성인인가요(성인이면 1, 미성년이면 0) : '))
if n == 1:
    print('당신은 성인입니다.')
elif n == 0:
    print('당신은 미성년자입니다.')
else:
    print('정수를 정확히 입력하세요.')

#LAB 3-4
#2
age = int(input('나이를 입력하시오 >> '))
if age > 10 and age < 19:
    print('청소년입니다.')

#윤년의 규칙
year = int(input('연수를 입력하시오 >> '))
if year % 400 == 0:
    print('윤년')
elif year % 4 == 0:
    if year % 100 == 0:
        print('평년')
    else:
        print('윤년')
else:
    print('연수를 정확히 입력하시오.')

#등급계산기
score = int(input('점수를 입력하시오 >> '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B' 
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print('당신의 등급은 :',grade)

#LAB 3-5
n = int(input('미세먼지 농도를 입력하시오 (단위 : microgram/m^3) >> '))
if n >= 76:
    print('매우 나쁨')
elif n >= 36:
    print('나쁨')
elif n >= 16:
    print('보통')
elif n >= 0:
    print('좋음')
else:
    print('다시 입력하시오.')


### 연습문제 ###
#3.6
a,b,c = input('세 정수를 입력하시오 >> ').split()
a = int(a)
b = int(b)
c = int(c)
if a > b:
    a,b = b,a
if b > c:
    b,c = c,b
if a > b:
    a,b = b,a
print(a,b,c)


#3.7
game_score = int(input('게임점수를 입력하시오 >> '))
if game_score >= 1000:
    print('고수입니다.')
else:
    print('입문자입니다.')

#3.8
x,y = input('점의 좌표 x, y를 입력하시오 >> ').split()
x = int(x)
y = int(y)
if (x>0) and (y>0):
    print('1사분면에 있음')
elif (x<0) and (y>0):
    print('2사분면에 있음')
elif (x<0) and (y<0):
    print('3사분면에 있음')
elif (x>0) and (y>0):
    print('4사분면에 있음')
else:
    print('원점의 좌표')

#3.9#
n = int(input('정수를 입력하시오 >> '))
if n % 2 == 0:
    print(f'{n}는(은) 2(으)로 나누어집니다.')
else:
    print(f'{n}는(은) 2(으)로 나누어지지 않습니다.')
if n % 3 == 0:
    print(f'{n}는(은) 3(으)로 나누어집니다.')
else:
    print(f'{n}는(은) 3(으)로 나누어지지 않습니다.')
if n % 2 == 0 and n % 3 == 0:
    print(f'{n}는(은) 2와(과) 3 모두에 대해 동시에 나누어집니다.')
else:
    print(f'{n}는(은) 2와(과) 3 모두에 대해 동시에 나누어지지 않습니다.')

#3.10
a,b = input('두 정수를 입력하시오 >> ').split()
a = int(a)
b = int(b)
if a%b == 0:
    print(a,'는(은)',b,'의 배수입니다.')
else:
    print(a,'는(은)',b,'의 배수가 아닙니다.')

#3.11
lotto = [2,3,9]
a,b,c = input('세 복권번호를 입력하시오 >> ').split()
a = int(a)
b = int(b)
c = int(c)
cnt = 0
lst = [a,b,c]
for i in lst:
    if i in lotto:
        cnt += 1

if cnt == 3:
    print('상금 1억')
elif cnt == 2:
    print('상금 1천만 원')
elif cnt == 1:
    print('상금 1만 원')
else: 
    print('다음 기회에...')


#3.12
x,y = input('점의 좌표 x, y를 입력하시오 >> ').split()
x = int(x)
y = int(y)
if (x**2 + y**2) ** (0.5) < 5:
    print('원의 내부에 있음')
else:
    print('원의 외부에 있음')

#3.13
x,y = input('점의 좌표 x, y를 입력하시오 >> ').split()
x = int(x)
y = int(y)
x1 = x - 3
y1 = y -4
if (x1**2 + y1**2) ** (0.5) < 10:
    print('원의 내부에 있음')
else:
    print('원의 외부에 있음')
'''
#3.14
a = input('알파벳을 입력하시오 >> ')
if a == 'a' or a == 'e'or a == 'i'or a == 'o'or a == 'u':
    print(a,'(은)는 모음입니다.')
else:
    print(a,'(은)는 자음입니다.')





















































