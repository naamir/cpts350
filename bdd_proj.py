from pyeda.inter import *

dectobindict = {
    0  : "0 0 0 0 0",
    1  : "0 0 0 0 1",
    2  : "0 0 0 1 0",
    3  : "0 0 0 1 1",
    4  : "0 0 1 0 0",
    5  : "0 0 1 0 1",
    6  : "0 0 1 1 0",
    7  : "0 0 1 1 1",
    8  : "0 1 0 0 0",
    9  : "0 1 0 0 1",
    10 : "0 1 0 1 0",
    11 : "0 1 0 1 1",
    12 : "0 1 1 0 0",
    13 : "0 1 1 0 1",
    14 : "0 1 1 1 0",
    15 : "0 1 1 1 1",
    16 : "1 0 0 0 0",
    17 : "1 0 0 0 1",
    18 : "1 0 0 1 0",
    19 : "1 0 0 1 1",
    20 : "1 0 1 0 0",
    21 : "1 0 1 0 1",
    22 : "1 0 1 1 0",
    23 : "1 0 1 1 1",
    24 : "1 1 0 0 0",
    25 : "1 1 0 0 1",
    26 : "1 1 0 1 0",
    27 : "1 1 0 1 1",
    28 : "1 1 1 0 0",
    29 : "1 1 1 0 1",
    30 : "1 1 1 1 0",
    31 : "1 1 1 1 1"
}

x = exprvars('x', 5)
y = exprvars('y', 5)

def edgeBF(i, j):
    print(i, "in binary")
    print(dectobindict[i].split())
    print(j, "in binary")
    print(dectobindict[j].split())

    fx = expr(x[0] & x[1] & x[2] & x[3] & x[4])
    fy = expr(y[0] & y[1] & y[2] & y[3] & y[4])
    bf = fx & fy
    bf = expr2bdd(bf)
    print("Boolean Formula:\n",bf)


    return bf

#E_9_12 = edgeBF(9,12)
#print(bdd2expr(E_9_12))
F = edgeBF(1, 4)  # first edge
for i in range(2, 32):
    j = (i + 3) % 32
    F = F | edgeBF(i,j)  # ORing all edges to create massive BF

for i in range(1, 32):
    j = (i + 7) % 32
    F = F | edgeBF(i,j)  # ORing all edges to create massive BF

print(F)
#f = truthtable(S, "00000001")
