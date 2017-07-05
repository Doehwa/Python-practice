


import random
n=random.randint(1,20)
numbers=int(input("수를 맞춰보세요"))
while n != numbers :
    if numbers > n:
        numbers = int(input("숫자가 너무 큽니다. 다른값을 입력하세요."))
    else:
        numbers = int(input("숫자가 너무 작습니다. 다른값을 입력하세요."))
if numbers == n:
        print("정답입니다.")
