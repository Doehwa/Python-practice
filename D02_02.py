# import turtle as t
# d=100
# a=90
# t.forward(d)
# t.left(a)
# t.forward(d)
# t.left(a)
# t.forward(d)
# t.left(a)
# t.forward(d)

# list_data =["재인", "철수", "준표", "재용", "도널드 트럼프"]
#
# print(list_data)
# # 재인 철수 준표 재용 도널드트럼희
# print(list_data[0])
# # 재인
# print(list_data[1])
# # 철수
# print(list_data[2])
# # 철수
# print(list_data[3])
# # 준표
# print(list_data[4][2])
# # 도널드 트럼프에서 드를 출력 배열 4에서 2번출력
# print(list_data[:])
# # 라인 15와 같은뜻
# print(list_data[1:3])
# # 재인 철수 준표 1부터 3전까지만
# print(list_data[:3])
# # 재인 철수 준표 0부터 3전까지만

list_data2=["재인", 25, [1, 2, 3, 4], ['재인', '철수']]

print(list_data2)
# ["재인", 25, [1, 2, 3, 4], ['재인', '철수']]
print(list_data2[0])
# 재인
print(list_data2[1])
# 25
print(list_data2[2])
# 1, 2, 3, 4
print(list_data2[3])
# 재인, 철수
print(list_data2[2][2])
# 3
print(list_data2[:])
# ["재인", 25, [1, 2, 3, 4], ['재인', '철수']]
print(list_data2[1:3])
# 25,[1, 2, 3, 4]
print(list_data2[:3])
# ["재인", 25, [1, 2, 3, 4]