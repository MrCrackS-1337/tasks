import sys

n = int(sys.argv[1])
m = int(sys.argv[2])

print(1, end='')
e = (m-1)%(n)
while e != 0:
    print(e+1, end='')
    e = (e + (m-1))%(n)
