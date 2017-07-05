string = "NATURE"
print("-"*5+"정방향"+"-"*5)
# -5정방향-5
print(string[0:5])
# NATUR
print(string[2:4])
# TU
print(string[2:])
# TURE
print(string[:3])
# NAT

print("-"*5+"역방향"+'-'*5)
print(string[-4:-2])
# 역방향은 0없이 센다.
print(string[-6:])
# NATURE
print(string[:-3])
# URE