a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

list(chain(a, b))

c = [iter(int, 1), iter(int, 1), iter(int, 1)]

from itertools import chain

x = chain(*map(lambda q: print(q), c))

list(x)

for i in x:
    print(i)
    break

for i in iter(int, 1):
    print(i)

