f = 0.796875
k = 1
list = list()

while (f > 0):
    f = 2*f
    d = int(f)
    list.append(int(f))
    f = f - d

print(list)

