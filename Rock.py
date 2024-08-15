import random

# 변수 선언
a = 'Rock'
b = 'Scissors'
c = 'paper'

print(a, b, c)

# 랜덤 숫자 출력
random_number = random.randint(1, 3)

print(random_number)

if random_number == 1:
    print(a)
else:
    print('done')