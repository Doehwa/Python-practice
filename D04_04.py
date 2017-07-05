# x=int(input("단을 입력하세요"))
# while x<10:
#     print("%d단을 시작합니다." % x)
#     k = 1
#     while k<10:
#
#         print(x*k)
#
#         k=k+1
#     if k==10 :
#         x=x+1
# if x==10 :
#     print("구구단이 끝났습니다.")


for x in range(2, 10):
    print("%d단을 시작합니다." % x)
    k = 1
    while k<10:

        print(k, "X ", x, "= ", x*k)

        k=k+1
    if k==10 :
        x=x+1
if x==10 :
    print("구구단이 끝났습니다.")

# for x in range(2, 10):
#     print(x, "X", 1,"=",x*1)