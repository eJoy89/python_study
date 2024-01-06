# def say_nick(nick):
#     if nick == '바보':
#         return 
#     print('나의 별명은 %s입니다' % nick)
    
# say_nick('바보')

# def say_myself(name, old, man = True):
#     print('나의 이름은 %s입니다' % name)
#     print('나이는 %d살입니다' % old)
#     if man:
#         print('남자입니다')
#     else:
#         print('여자입니다')
        
# say_myself('조윤재', 34, True)

# a = 3
# def vartest():
#     global a
#     a = a + 1
#     return a
# vartest()    
# print(a)


# add = lambda a, b: a + b
# result = add(3, 4)
# print(result)

# def add(a, b):
#     return a + b

# result = add(3, 4)
# print(result)

# check = add(8, 10)
# print(check)


# def multiply(a, b):
#     return a * b

# print(multiply(365, 20))

# def text():
#     return 'text testing'
# print(text())

def text(text):
    return text + ' function'

print(text('Sentence'))

def account(num):
    number_string = str(num)
    parts = number_string.split(".")
    parts[0] = "{:,}".format(int(parts[0]))
    
    return ",".join(parts)

print(account(1000000))