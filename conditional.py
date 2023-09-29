# money = True
# if money:
#     print('get a cap')
# else:
#     print('walking')


# money = 1
# if money:
#     print('택시를')
#     print('타고')
#     print('가라')
    
    
# x = 3
# y = 2

# print(x > y)
# print(x < y)
# print(x == y)


# money = 900
# if money >= 1000:
#     print('take a cap')
    
# else: 
#     print('take a walk')

# money = 2000
# card = False
# if money > 2000 or card:
#     print('take a cap')
# else:
#     print('take a walk')
    

# print(1 in [1, 2, 3])

# print(1 not in [1, 2, 3])


# print('a' in ['a', 'b', 'c'])
# print('a' not in ['a', 'b', 'c'])

# pocket = ['papper', 'money', 'cellphone']

# # if 'money' in pocket:
# if 'no money' in pocket:
#     pass

# else:
#     print('by Card')


pocket = ['paper', 'cellphone', 'money']

card = True

if 'money' in pocket:
    print('take a taxi')
else:
    if card:
        print('take a taxi1')
    else:
        print('take a walk')