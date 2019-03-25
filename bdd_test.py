from pyeda.inter import *

x1 = bddvar('x1')
x2 = bddvar('x2')
x3 = bddvar('x3')
x4 = bddvar('x4')
x5 = bddvar('x5')

y1 = bddvar('y1')
y2 = bddvar('y2')
y3 = bddvar('y3')
y4 = bddvar('y4')
y5 = bddvar('y5')

z1 = bddvar('z1')
z2 = bddvar('z2')
z3 = bddvar('z3')
z4 = bddvar('z4')
z5 = bddvar('z5')

f = expr("x1 & x2 & x3 & x4 & x5 & ~y1 & ~y2 & y3 & y4 & ~y5")
f1 = expr2bdd(f)

print(bdd2expr(f1.compose({y1:z1, y2:z2, y3:z3, y4:z4, y5:z5})))