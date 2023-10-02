# treeHit = 0
# while treeHit < 10:
#     treeHit = treeHit + 1
#     print("나무를 %d번 찍었습니다" % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다")
        
        
        
# prompt = """
# 1. Add
# 2. Del
# 3. List
# 4. Quit
# """

# number = 0
# while number != 4:
#     print(prompt)
#     number int(input())
    
# 1. Add
# 2. Del
# 3. List
# 4. Quit

# Enter number: 5

# Enter number:
# 1

# 1. Add
# 2. Del
# 3. List
# 4. Quit


coffee = 10
money = 300
while money:
    print('돈을 받았으니 커피를 줍니다.')
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다" % coffee)
    if coffee == 0:
        print('no coffee')
        break