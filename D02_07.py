strdata = 'time is money!'
print(strdata[::2])
# 두칸마다 선택.(공백)
print(strdata[::3])
# 세칸마다 선택(공백)

# 시퀀스 자료 연결
strdata1 = "I Love " ; strdata2 = "python" ; strdata3 ="you"
listdata1=[1,2,3]; listdata2=[4,5,6]
print(strdata1+strdata2)
print(strdata1+strdata3)
print(listdata1+listdata2)

artist ="빅뱅"
sing="뱅~"
a= artist + "이 부르는 " + sing*3
print(a)

# 시퀀스 자료크기이해
strdata1 = 'I love python'
strdata2 = '나는 파이썬을 사랑합니다'
listdata = ["a", "b","c", strdata1, strdata2]
print(len(strdata1))
print(len(strdata2))
print(len(listdata))
print(len(listdata[3]))