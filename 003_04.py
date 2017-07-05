
# 문자열을 위한 메서드

myStr = "Hello, My little princess"
print(myStr.upper())
# 메서드. 스트링에 대해 명령을 내림.
print(myStr.lower())
print(myStr.title())


print(myStr.count('b'))
print(myStr.endswith('s'))
# y로 끝나는 것을 출력하라
print(myStr.startswith('h'))
# H로시작하는것을 출력하라.

cheesses = ["체다", "모짜렐라", "까망베르", "리코타"]
print(cheesses)
# ["체다", "모짜렐라", "까망베르", "리코타"]
cheesses[0] = '크림'
# ["크림", "모짜렐라", "까망베르", "리코타"]

all = cheesses+["블루"]
print(all)
# ["크림", "모짜렐라", "까망베르", "리코타", "블루"]
print(cheesses)
# ["크림", "모짜렐라", "까망베르", "리코타"]

