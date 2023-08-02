import sys

n = int(sys.argv[1])
m = int(sys.argv[2])


def sequence(n, m):
    yield 1
    for i in range(m-1, n*m, m-1):
        num = i % n + 1
        if num == 1:
            return
        yield num


path = list(sequence(n, m))
for j in path:
    print(j, end="")
