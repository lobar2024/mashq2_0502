# 1) RO‘YXATNI JUFT VA TOQLARGA AJRATISH
a = list(map(int, input().split()))
juft, toq = [], []

for x in a:
    if x % 2 == 0:
        juft.append(x)
    else:
        toq.append(x)

print(juft)
print(toq)
