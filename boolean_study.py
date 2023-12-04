# a = [1, 2, 3, 4]
# while a:
#     print(a.pop())
    
    
# if[1, 2, 3]:
#     print('true')
# else: 
#     print('false')
    
    
    
# if[]:
#     print('true')
# else: 
#     print('false')
    
    
# bool([1, 2, 3])
# bool([])
# bool(0)
# bool(2)
# print('------------')


# b = [1, 2, 3]
# print(id(b))

# c = [1, 2, 3]
# d = c
# print(id(c))
# print(id(d))

# a = [1, 2, 3]
# # b = a[:]
# b = a

# a[1] = 4
# print(a)
# print(b)


# from copy import copy

# a = [1, 2, 3]
# b = copy(a)
# print(a, b)

# c = 'gg'
# d = copy(c)
# print(d)




# a, b = ('python', 'life')
# (a, b) = 'python', 'life'
# [a, b] = ['python', 'life']
# a = b = 'python'

# print(a)
# print(b)

from copy import copy
a = [1, 2, 3]
b = a

print(a is b)

print(a)