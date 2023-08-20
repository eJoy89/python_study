a = { 'name': 'py', 'phone': '01100000000', 'birth': '1118' }

print(a)

print('name' in a )
print('email' in a )

s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2)

s3 = set([ 1, 2, 3, 4, 5 ])
s4 = set([ 4, 5, 6, 7, 8 ])

print(s3 & s4)
print(s3.intersection(s4))
print(s3 | s4)
print(s3.union(s4))

print(s3 - s4)

print(s3)
print(s3.remove(3))
print(s3)