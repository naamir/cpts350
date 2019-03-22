from pyeda.inter import *
import time

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

#x = exprvars('x', 5)
#y = exprvars('y', 5)

def edgeBF(i, j):
    print(i, "in binary")
    print(dectobindict[i].split())
    print(j, "in binary")
    print(dectobindict[j].split())

    if int(dectobindict[i].split()[0]) == 0:
        fx = "~x1"
    else:
        fx = "x1"

    if int(dectobindict[i].split()[1]) == 0:
        fx = fx + " & ~x2"
    else:
        fx = fx + " & x2"

    if int(dectobindict[i].split()[2]) == 0:
        fx = fx + " & ~x3"
    else:
        fx = fx + " & x3"

    if int(dectobindict[i].split()[3]) == 0:
        fx = fx + " & ~x4"
    else:
        fx = fx + " & x4"

    if int(dectobindict[i].split()[4]) == 0:
        fx = fx + " & ~x5"
    else:
        fx = fx + " & x5"


    if int(dectobindict[j].split()[0]) == 0:
        fy = "~y1"
    else:
        fy = "y1"

    if int(dectobindict[j].split()[1]) == 0:
        fy = fy + " & ~y2"
    else:
        fy = fy + " & y2"

    if int(dectobindict[j].split()[2]) == 0:
        fy = fy + " & ~y3"
    else:
        fy = fy + " & y3"

    if int(dectobindict[j].split()[3]) == 0:
        fy = fy + " & ~y4"
    else:
        fy = fy + " & y4"

    if int(dectobindict[j].split()[4]) == 0:
        fy = fy + " & ~y5"
    else:
        fy = fy + " & y5"


#     #print("x[0]", x[0])
#     #fx = x1 + " & " + x2 + " & " + x3 + " & " + x4 + " & " + x5
#     #fy = y1 + " & " + y2 + " & " + y3 + " & " + y4 + " & " + y5
    bf = fx + " & " + fy
    print("Boolean Formula for Edge({}, {}):\n".format(i,j) ,bf)
    bf = expr(bf)
    #bf = expr2bdd(bf)
    print("Boolean Formula:\n",bf)


    return bf


F = edgeBF(1, 4)  # first edge
for i in range(2, 32): # edge condition 1
    j = (i + 3) % 32
    F = F | edgeBF(i,j)  # ORing all edges to create massive BF

for i in range(1, 32): # edge condition 2
    j = (i + 7) % 32
    F = F | edgeBF(i,j)  # ORing all edges to create massive BF

#print("F:\n", F)

print("\nFull BF -> F:\n", F)

R = expr2bdd(F)
print("R:\n", R)

# now we get the Transistive Closure R*
x1 = bddvar('x1', 0)
x2 = bddvar('x2', 0)
x3 = bddvar('x3', 0)
x4 = bddvar('x4', 0)
x5 = bddvar('x5', 0)

y1 = bddvar('y1', 0)
y2 = bddvar('y2', 0)
y3 = bddvar('y3', 0)
y4 = bddvar('y4', 0)
y5 = bddvar('y5', 0)

z1 = bddvar('z1', 0)
z2 = bddvar('z2', 0)
z3 = bddvar('z3', 0)
z4 = bddvar('z4', 0)
z5 = bddvar('z5', 0)

def compose(R1, R2):
    R1.compose({y1:z1, y2:z2, y3:z3, y4:z4, y5:z5})
    R2.compose({x1:z1, x2:z2, x3:z3, x4:z4, x5:z5})

    R3 = R1 & R2

    R4 = R3.smoothing({z1,z2,z3,z4,z5})

    return R4

def getRstar(R):
    H = R

    while True:
        Hp = H
        H = Hp | compose(Hp, R)
        print("H:\n", list(H.satisfy_all()))
        time.sleep(3)
        if (H == Hp):
           break
    
    return H

R_star = getRstar(R)
print(R_star)

#print(list(R_star.satisfy_all()))





