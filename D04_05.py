k= int(input("구구단 몇단을 출력할까요? 숫자를 입력하세요"))
while k<2 or k>9:
    k=int(input("구구단에 유효하지 않은 숫자입니다. 다시 입력하세요"))
for x in range(1, 10):
    print(k, "X", x, "=", x * k)
