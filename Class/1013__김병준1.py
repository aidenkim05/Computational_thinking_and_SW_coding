#1013_김병준
#6장 리스트 수업
'''
#리스트 자료형의 필요성
score_list = [87, 84, 95, 67, 88, 94, 63]
print(score_list)
print(score_list[0], score_list[3])

list1 = list()
list2 = []
list3 = list((1,2,3))
list4 = list(range(1,10))
list5 = list('ABCDEF')

#LAB 6-1
#1
even_list = [2,4,6,8,10]
print(even_list)
#2
even_list = list(range(2,11,2))
print(even_list)
#3
nations = ['Korea','China','India','Nepal']
print(nations)
#4
friends = ['길동','철수','은지','지은','영민']
print(friends)
#5
strings = list('XYZ')
print(strings)

#리스트와 인덱스
a = [11,22,33,44,55,66]     #최대 인덱스는 len(n_list) - 1
print(a)
print(len(a))
print(a[0])

a = [11,22,33,44,55,66]     #음수 인덱스
print(a[-1])
print(a[-2])
print(a[-3])

#LAB 6-2
#1
prime_list = [2,3,5,7]
print(f'prime_list의 첫 원소 : {prime_list[0]}')
#2
print(f'prime_list의 마지막 원소 : {prime_list[3]}')
#3
print(f'prime_list의 마지막 원소 : {prime_list[-1]}')
print()
#4
nations = ['Korea','China','Russia','Malaysia']
print(f'nations의 첫 원소 : {nations[0]}')
#5
print(f'nations의 마지막 원소 : {nations[-1]}')
#6
print(f'nations의 마지막 원소 : {nations[len(nations)-1]}')

#리스트 항목의 추가와 삭제
#append() 메소드
a_list = ['a','b','c','d','e']
print(a_list)
a_list.append('f')
print(a_list)
print()

n_list = [10,20,30,40]
print(n_list)
n_list.append(50)
print(n_list)

#del 키워드로 삭제
n_list = [11,22,33,44,55,66]
print(n_list)
del n_list[3]       #지정된 인덱스에 위치한 항목 삭제
print(n_list)

#remove() 메소드로 삭제
n_list = [11,22,33,44,55,66]
print(n_list)
n_list.remove(44)   #특정한 값을 리스트의 항목에서 삭제
print(n_list)       #존재하지 않는 항목 삭제하면 오류 발생

#pop() 메소드
n_list = [11,22,33,44,55,66]
print(n_list)
n_list.pop()        #가장 마지막 항목 삭제
print(n_list)

#멤버 연산자 : in, not in
a_list = [10,20,30,40]
print(10 in a_list)
print(50 in a_list)
print(10 not in a_list)
print(50 not in a_list)
print()

n_list = [11,22,33,44,55,66]
if (55 in n_list):
    n_list.remove(55)
if (88 in n_list):
    n_list.remove(88)
print(n_list)

#LAB 6-3
#1
prime_list = [2,3,5,7]
print(f'소수 목록 : {prime_list}')
prime_list.append(11)
print(f'추가 후 소수 목록 : {prime_list}')
#2
print(f'삭제 전 소수 목록 : {prime_list}')
prime_list.remove(3)
print(f'삭제 후 소수 목록 : {prime_list}')
print()
#3
nations = ['Korea','China','Russia','Malaysia']
print(f'국가 목록 : {nations}')
nations.append('Nepal')
print(f'추가 후 국가 목록 : {nations}')
#4
if 'Japan' in nations:
    print('Japan는(은) 국가 목록에 있습니다.')
else:
    print('Japan는(은) 국가 목록에 없습니다.')
if 'Russia' in nations:
    print('Russia는(은) 국가 목록에 있습니다.')
else:
    print('Russia는(은) 국가 목록에 없습니다.')

#리스트에 적용되는 내장함수
list1 = [20,10,40,50,30]
print(min(list1))
print(max(list1))
print(sum(list1))

fruits = ['banana','orange','apple','kiwi']
print(min(fruits))
print(max(fruits))

k_fruits = ['사과','귤','포도','참외']
print(min(k_fruits))
print(max(k_fruits))

#LAB 6-4
#1
prime_list = [2,3,5,7]
print(f'1에서 10까지의 소수 : {prime_list}')
print(f'최솟값 : {min(prime_list)}')
print(f'최댓값 : {max(prime_list)}')
print(f'합계 : {sum(prime_list)}')
print(f'평균 : {sum(prime_list)/len(prime_list)}')
#2
nations = ['Korea','China','Russia','Malaysia']
print(f'국가 목록 : {nations}')
print(f'사전에 가장 먼저 나오는 나라 : {min(nations)}')
print(f'사전에 가장 뒤에 나오는 나라 : {max(nations)}')

#리스트의 메소드
#sort() 메소드
list1 = [20,10,40,50,30]
list1.sort()
print(list1)
list1.sort(reverse = True)
print(list1)

#index() 메소드
a_list = ['a','b','c','d','e']
print(a_list.index('a'))
print(a_list.index('b'))

#count() 메소드
b_list = ['a','b','c','a','b','a']
print(b_list.count('a'))
print(b_list.count('b'))

#extend() 메소드
list1 = ['a','b','c']
list2 = [1,2,3]
list1.extend(list2)
print(list1)
list1.extend('d')
print(list1)

#insert() 메소드
list1 = ['a','b','c']
list1.insert(1,'b')
print(list1)

#pop() 메소드
list1 = ['a','b','c','d']
print(list1.pop())
print(list1)
list1 = ['a','b','c','d']
print(list1.pop(1))
print(list1)

#reverse() 메소드
list1 = [10,20,30,40]
list1.reverse()
print(list1)

#LAB 6-5
#1
a = [1,2,3]
b = [10,20,30]
a.append(b)
print(a)
print()
a = [1,2,3]
b = [10,20,30]
a.extend(b)
print(a)
print()
#2
nlist = list(range(1,11))
print(f'nlist = {nlist}')
#3
nlist.insert(0,0)
print(f'nlist = {nlist}')
#4
nlist.sort(reverse = True)
print(f'마지막 원소 : {nlist[-1]}')
nlist.pop()
print(f'nlist = {nlist}')

#리스트와 연산
#두 리스트 합치는 연산자 +
list1 = [11,22,33,44]
list2 = [55,66]
list3 = list1 + list2
print(list3)

#리스트의 곱셈 연산
list1 = [1,2,3,4]
print('list1 * 2 =',list1 * 2)
print('list1 * 3 =',list1 * 3)
#list1 * list2      리스트끼리의 곱셈은 불가능

#리스트의 비교연산
list1 = [1,2,3,4]
list2 = [1,2,3,4]
print(list1 == list2)
list3 = [4,1,2,3]
print(list1 == list3)

#리스트의 크기 비교
list1 = [1,2,3,4]
list2 = [2,3,3,4]
print(list1 > list2)
print(list1 < list2)

#LAB 6-6
#1
list1 = [1,2,3]
n = int(input("반복할 정수를 입력하시오 >> "))
print(list1 * n)

#리스트의 내용 갱신을 위한 방법
list1 = [10,20,30,40,50]
i = 0
for n in list1:
    list1[i] = n * 10
    i += 1
print(list1)

list1 = [10,20,30,40,50]
list1 = [n * 10 for n in list1]     #고급 기능
print(list1)

#리스트의 슬라이싱
#슬라이싱 >> 리스트_이름[start:end] (end-1까지)
a_list = [10,20,30,40,50,60,70,80]
print(a_list[1:5])
print(a_list[0:1])
print(a_list[0:2])
print(a_list[0:5])
print(a_list[1:])
print(a_list[:5])
print(a_list[:])        #모든 항목

#음수 인덱스를 사용한 슬라이싱
a_list = [10,20,30,40,50,60,70,80]
print(a_list[-7:-2])
print(a_list[-7:])
print(a_list[:-2])
print(a_list[:-2] + a_list[-2:])    #슬라이싱 덧셈
print(a_list[-2:] + a_list[:-2])

#슬라이싱에 사용하는 스텝
a_list = [10,20,30,40,50,60,70,80]
print(a_list[0::3])
print(a_list[::-1])

#LAB 6-7
#1
n_list = list(range(15))
print(f'n_list = {n_list}')
#2
print(n_list[0:5])
print(n_list[5:11])
print(n_list[11:15])
print(n_list[2:11:2])
print(n_list[10:5:-1])
print(n_list[10:1:-2])
'''
'''
#연습문제
#6.1
list_ex=[10,20,30,40,50,60,70]
high=5
low=3
print(list_ex[low])
print(list_ex[low+2])
print(list_ex[high-low])
print(list_ex[low-high])
print(list_ex[-1])
print(list_ex[-low])
print(list_ex[2*3])
print(list_ex[2]*3)
print(list_ex[5%4])
print(len(list_ex))

#6.2
spell=['s','w','e','e','t']
print(spell)
spell[3]='a'
print(spell)
spell[4]='r'
print(spell)
print(spell*2)

#6.3
list1 = [3,5,7]
list2 = [2,3,4,5,6]
for i in range(3):
    for j in range(5):
        print(f'{list1[i]} * {list2[j]} = {list1[i] * list2[j]}')

#6.4
a = [2,3,4,5,6]
rev_a = []
for i in range(len(a)):
    rev_a.append(a.pop())
print(rev_a)

#6.5
list1 = ['I like', 'I love']
list2 = ['pancakes.', 'kiwi juice.', 'espresso.']
for i in range(len(list1)):
    for j in range(len(list2)):
        print(f'{list1[i]} {list2[j]}')

#6.6
list1 = [2,3,4,1,32]
print(max(list1))
print(sum(list1))
list1.remove(32)
print(list1)
list1.reverse()
print(list1)
list1.sort()
print(list1)

#6.7
n_list = [10,20,30,50,60]
print(f'리스트 원소들 : {n_list}')
hap = 0
for i in range(len(n_list)):
    hap += n_list[i]
print(f'리스트 원소들의 합 : {hap}')

#6.8
n_list = [10,20,30,50,60]
print(f'리스트 원소들 : {n_list}')
gop= 1
for i in range(len(n_list)):
    gop *= n_list[i]
print(f'리스트 원소들의 곱 : {gop}')

#6.9
n_list = [10,20,30,50,60]
print(f'리스트 원소들 : {n_list}')
n_max=0
for n in n_list:
    if n>n_max:
        n_max=n
print('리스트 원소들 중 최대값:',n_max)        

#6.10
n_list = [10,20,30,50,60]
print(f'리스트 원소들 : {n_list}')
n_min=9999999999
for n in n_list:
    if n<n_min:
        n_min=n
print('리스트 원소들 중 최소값:',n_min)

#6.11
number = list(map(int,input('5개 수 입력 >> ').split()))
print(f'합 : {sum(number)}')
print(f'합 : {sum(number)/len(number)}')
print(f'최댓값 : {max(number)}')
print(f'최솟값 : {min(number)}')


## 과제
#6.18
#1
s_list = ['abc','bcd','bcdefg','abba','cddc','opq']
min_str = s_list[0]
for i in range(1,len(s_list)):
    if len(min_str) > len(s_list[i]):
        min_str = s_list[i]
print(f'(1). 가장 길이가 짧은 문자열 : {min_str}')
#2
max_str = s_list[0]
for i in range(1,len(s_list)):
    if len(max_str) < len(s_list[i]):
        max_str = s_list[i]
print(f'(2).가장 길이가 긴 문자열 : {max_str}')
#3
s_list = ['abc','bcd','bcdefg','abba','cddc','opq']
s_list.sort(key=len)
shortest_3 = s_list[:3]
print(f'(3). 길이가 가장 짧은 문자열 3개: {shortest_3}')

#6.22
def snake_array():
    n = int(input("1부터 10까지의 정수 n을 입력하시오: "))
    number = 1
    for i in range(n):
        if i % 2 == 0:
            row = list(range(number, number + n))
            for num in row:
                print(f'{num:<4}', end='')
            print()
            number += n
        else:
            row = list(range(number, number + n))
            row_reversed = row[::-1]
            for num in row_reversed:
                print(f'{num:<4}', end='')
            print()
            number += n
snake_array()

#6.23
person1 = ['온달', 20, 1, 180.0, 100.0]
person2 = ['이사부', 25, 1, 170.0, 70.0]
person3 = ['평감', 22, 0, 180.0, 60.0]
person4 = ['혁거세', 40, 1, 180.0, 50.0]
#1
def how_many_persons(person_list):
    return len(person_list) // 5
person_list = person1 + person3 + person4
n_persons = how_many_persons(person_list)
print('(1). ' + str(n_persons) + '명의 정보가 담겨 있습니다.')
#2
def compute_average_age(person_list):
    ages = person_list[1::5]
    total_age = sum(ages)
    num_persons = len(ages)
    return total_age / num_persons
person_list = person1 + person2 + person3 + person4
average_age = compute_average_age(person_list)
print('(2). 평균 나이는 ' + str(average_age) +'세입니다.')
#3
def count_males_females(person_list):
    n_male = 0
    n_female = 0
    genders = person_list[2::5]
    for gender in genders:
        if gender == 1:
            n_male += 1
        else:
            n_female += 1     
    return n_male, n_female
person_list = person1 + person2 + person3 + person4
n_male, n_female = count_males_females(person_list)
print('(3). 리스트에는 남자가', n_male,'명, 여자가', n_female, '명입니다.')
#4
def display_persons(person_list):
    for i in range(0, len(person_list), 5):
        person_info = person_list[i:i+5]
        print(person_info)
person_list = person1 + person2 + person3 + person4
print('(4).')
display_persons(person_list)

#6.24
def find_perfect_numbers(limit):
    for number in range(2, limit + 1):
        proper_divisors = []
        divisors_sum = 0
        for i in range(1, number):
            if number % i == 0:
                proper_divisors.append(i)
                divisors_sum += i
        if divisors_sum == number:
            print(f"{number}은 완전수입니다.")
            print(f"{number}의 진약수 : {proper_divisors}, 약수의 합 = {divisors_sum}")
find_perfect_numbers(10000)
'''



































