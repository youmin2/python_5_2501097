#32
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

c = a|b
d = a&b

print(c, d)

#33
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

c = a-b
d = a^b

print(c, d)

#34
a = {1, 2, 3, 4, 5}
a |= {100}

print(a)

#35
a = {100, 200, 300, 400, 500}

a &= {400, 500, 600, 700, 800}
a -= {400, 500, 600, 700, 800}
a ^= {400, 500, 600, 700, 800}

print(a)

#36
a = {100, 200, 300, 400, 500}
b = {100, 200, 300, 400, 500}

if (a >= b) and (a <= b):
    print("동시")
elif a >= b:
    print("상위")
elif a <= b:
    print("부분")

#37
a = {1, 2, 3, 4, 5}
a.add(1000)
a.remove(1000)

print(a)

#38
multiples = {x for x in range(1, 101)if x % 3 == 0 and x % 5 == 0}

print(multiples)
