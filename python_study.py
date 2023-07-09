a = "Life is too short, You need Python"
b = a[5] + a[6]
c = a[-6] + a[-5] + a[-4] + a[-3] + a[-2] + a[-1]
d = a[8:11]
e = a[0:]

print(a[0], a[1], a[2], a[3])
print(b)
print(c)
print(d)
print(e)


format = "I eat %d apples." %7
format1 = "I ate %s cherries" % "six"

num = 7
format2 = "I had %s melons" % num

day = 'two'
format3 = "I ate %d apples. so I was sick for %s days" %(num, day)

print(format)
print(format1)
print(format2)
print(format3)

wordLeng = 'apple'

print(','.join(wordLeng))

print(a.split())