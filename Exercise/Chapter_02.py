#변수와 연산자
'''
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
'''
#2.12
Pi = 3.141592
r = 11
l = 2*(Pi*r)
print('원의 반지름 =',r)













