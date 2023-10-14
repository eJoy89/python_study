# test_list = [ 'one', 'two', 'three' ]
# for i in test_list:
#     print(i)
    
# a = [ (1, 2), (3, 4), (5, 6) ]
# for(frist, second) in a:
#     print(frist + second)

# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark >= 60:
#         print('%d번 학생은 합격입니다' % number)
#     else:
#         print('%d번 학생은 불합격입니다' % number)
        
# for mark in marks:
#     number = number + 1
#     if mark < 60: continue
#     print('%d번 학생 축하합니다. 합격입니다' % number)

# a = range(10)
# # print(list(a))

# add = 0
# for i in a:
#     add = add + i
# print(add)

for i in range(2, 10):
    for j in range(1, 10):
        # print(i * j)
        print(i*j, end= " ")
    print('')