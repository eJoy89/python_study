a = []
b = [1, 2, 3]
c = ['life', 'is', 'too', 'short']
d = [1, 2, 'life', 'is']
e = [1, 2, ['life', 'is']]
f = [1, 2, 3, 4, 5, 6, 7, 8]
g = [3, 5, 6, 1, 4, 2]
h = [1, 2, 3, 4, 1, 2, 3, 4, 3, 3, 3]
i = [1, 2, 3]

print(b[1] + d[0])
print(e[2])
print(e[2][0])
print(e[2][1])

print(f[1:4])
print(f[:5])
print(f[5:])

print(b + f)
print(f*3)
print(len(f))
b[1] = 7
print(b)

del b[1]
print(b)

del f[:4]
print(f)

b.append('good')
print(b)

b.append(['bad', 'strange'])
print(b)

g.sort()
print(g)

b.insert(0, 7)
print(b)

h.remove(2)
print(h)

print(i)
i.pop(2)
print(i)

print(h.count(3))