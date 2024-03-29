alist = [['a', 10], ['b', 2], ['c', 30], ['d', 4]]
x = []
y = []
out = []

for i in alist:
    x.append (i[-1])

x.sort()
# print(x)
for i in alist:
    for j in x[:2]:
        if j == i[-1]:
            y.append(i)
for i in y:
    out.append(i[0])
print(*out)

