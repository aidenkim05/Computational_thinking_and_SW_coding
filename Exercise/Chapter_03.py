#조건문

#3.1#

#3.2
n = input("이름을 입력하시오 >> ")
h = int(input("키를 입력하시오 (단위 cm) >> "))
if h >= 140:
    print(n,'님은 놀이기구를 탈 수 있습니다.')
else:
    print(n,'님은 놀이기구를 탈 수 없습니다.')

#3.3
age = int(input("나이를 입력하시오 >> "))
h = int(input("키를 입력하시오 (단위 cm) >> "))
if (age >= 19) and (h >= 150):
    print('입장할 수 있습니다.')
else:
    print('입장할 수 없습니다.')

#3.4
age = int(input("나이를 입력하시오 >> "))
if age >= 20:
    print('Adult')
elif age > 10:
    print('Youth')
else:
    print('Kid')

#3.5
a,b = input('두 정수를 입력하시오 >> ').split()
a = int(a)
b = int(b)
if a >= b:
    print(b,a)
else:
    print(a,b)

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

#3.11#
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

#3.14
a = input('알파벳을 입력하시오 >> ')
if a == 'a' or a == 'e'or a == 'i'or a == 'o'or a == 'u':
    print(a,'(은)는 모음입니다.')
else:
    print(a,'(은)는 자음입니다.')
