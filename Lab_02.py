#변수와 연산자

#LAB 2-1
print('나의 이름은 :', '김병준')
print('나의 나이는 : ', 21)
print('나의 키는 :',182, 'cm 입니다.')
print('10 + 20 =',10 + 20, '10 * 20 =',10 * 20)

#LAB 2-2
Pi = 3.14
r = 8.0
s = Pi * r **2
l = 2 * Pi * r
print('원의 반지름',r)
print('원의 면적',s)
print('원의 둘레',l)

#LAB 2-3
#3
width = 100
height = 200
s = width * height
print('너비',width,', 높이',height,'인 사각형의 면적 :',s)

#LAB 2-4
name = '김병준'
print('나의 이름은 :', name)
age = 21
print('나의 나이는 :',age)
height = 182
print('나의 키는', height,'cm 입니다.')
sum = 10 + 20
print('10 + 20 =',sum)
mult = 10 * 20  
print('10 * 20 =', mult)

#LAB 2-5
#2
w = 20
h = 40
area = w * h
print('사각형의 면적',area)

#LAB 2-6
w = 20
h = 40
w = 30
area = w * h
print('사각형의 면적',area)

#LAB 2-7
#1
print(123 * 456)
print(1357 + 2468)
print(5 ** 4)
print(20 / 4)
print(20 // 5)
print(20 % 5)
#2
print(5 % 2)
#3
print(2 ** 0.5)
print(2 ** (1/2))
print(3 ** 0.5)
print(3 ** (1/2))

#LAB 2-8
a = 8 + 2j      #VS Code에서 파이썬 복소수는 j를 사용하여 실수부+허수부j 형식으로 작성
b = 4 + 3j
print(a + b)
print(a - b)
print(a * b)
print(a / b)

#LAB 2-9
a = 1024
print(a)
print(a>>2)
a = a >> 1
print(a)
a = a >> 1
print(a)

a = 1
print(a<<1)
a = a<<1
print(a)
a = a<<1
print(a)
a = a<<1
print(a)

#LAB 2-10
#1
name = input("이름을 입력하세요 >> ")
print(name,"님이 입장하셨습니다.")
#2
m = int(input("숫자 m을 입력하세요 >> "))
n = int(input("숫자 n을 입력하세요 >> "))
print('m + n =', m+n)
print('m - n =', m-n)
#3
r = int(input('원의 반지름을 정수로 입력하세요 >> '))
print("원의 반지름 :", 3.14*r*r)