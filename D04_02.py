

# 정답은 8
x=int(input("수를 입력하세요"))
while x!=8:
    if x>8 :
        x = int(input("숫자가 너무 큽니다. 다른값을 입력하세요."))
    else :
        x=int(input("숫자가 너무 작습니다. 다른값을 입력하세요."))
if x==8:
    print("정답입니다.")