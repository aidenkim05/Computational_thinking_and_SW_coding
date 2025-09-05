#파이썬 소개

#1.3
print(100)
print(100+200)
print('100 + 200')
print(100,200)
print('100','200')
print('100''200')
print('Hello Python!')
print('Hello','Python','!')
print('Hello'+'Python'+'!')
print('Hello''Python''!')
print('**********')
print('*'*10)

#1.4
print('Hello Python')

#1.5
print('Welcome To Python!')
print('Welcome To Python!')
print('Welcome To Python!')
print('Welcome To Python!')
print('Welcome To Python!')

#1.6
print('*'*20)
print('안녕하세요~')
print('저는 김병준입니다.')
print('경북대학교 전자공학부 인공지능전공 2학년입니다.')
print('*'*20)

#1.7
j = 3
for i in range(1,8,2):
    print(' '*j + '*'*i)
    j -= 1
    
#1.8
j = 0
for i in range(7,0,-2):
    print(' '*j + '*'*i)
    j += 1    
    
#1.9
print(400-200)
print(45*89)
print(32/8)
print(9*3)
print(9**3)
print(9/3)
print(9//3)
print(9%3)

#1.10
#(1)
sum = 0
for i in range(1,11):
    sum += i
print(sum)
#(2)
Pi = 3.14
r = 5
print(2 * Pi * r)
#(3)
l = 25
print(4*l)
#(4)
l = 25
print(l**2)
#(5)
h = 10
l = 30
print(2*(h+l))
#(6)
h = 10
l = 30
print(h*l)

#1.11
v = 80
h = 1.5
r = v*h
print('주행거리 :',r,'km')

#1.12
h = 2
r = 190
v = r/h
print('평균속력 :',v,'km/h')

#1.13
r = 149597870
v = 299792
h = r/v
print('걸린 시간 :',h,'초')

#1.14
def factorial(n):
    result = 1
    for i in range(n,0,-1):
        result *= i
    return result

print(factorial(3))
print(factorial(5))
print(factorial(12))
print(factorial(20))

#1.15
def mean_values(a,b):
    result = (a+b)/2
    return result

print('100과 200의 평균값 :',mean_values(100,200))

#1.16
print('50 + 30 = ', 50 + 30)
print('50 - 30 = ', 50 - 30)
print('50 * 30 = ', 50 * 30)
print('50 / 30 = ', 50 / 30)

#1.17
def calculate(a,b):
    print(a, '+', b, '=', a+b)
    print(a, '-', b, '=', a-b)
    print(a, '*', b, '=', a*b)
    print(a, '/', b, '=', a/b)

calculate(3,6)
calculate(10,30)
calculate(8000,2000)
calculate(12000,2000)
calculate(80000000,20000000)


