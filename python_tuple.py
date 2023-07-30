t1 = ()
t2 = (1,)
t3 = (1, 2, 3)

print(t1, t2, t3)


print(t3)
print(t3[1])


# Dictionary

dic = { 'name': 'Cho', 'phone': '010-xxxx-xxxx', 'birth' : '0912' }
print(dic)

print(dic['name'])
print(dic['phone'])
print(dic['birth'])
print(dic.keys())


a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'cho'
print(a)

del a['name']
print(a)