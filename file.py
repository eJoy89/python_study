# f = open('testing.txt', 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다\n" % i
#     f.write(data)
#     print(data)
# f.close()

# for i in range(1, 11):
#     data = '%d번째 줄입니다\n' % i
#     print(data)

# f = open('새파일3.txt', 'w')
# for i in range(1, 11):
#     data = "이것은 %d번쨰 줄 입니다.\n" % i
#     f.write(data)
# f.close()


# f = open('새파일3.txt', 'r')
# line = f.readline()
# print(line)
# f.close()

f = open('새파일3.txt', 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()