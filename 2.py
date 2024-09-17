from z3 import *
Q = []
for i in range(8):
    Q.append(Int('Q_%i' % (i + 1)))

val_c = []
for i in range(8):
    val_c.append(And(1 <= Q[i], Q[i] <= 8))

col_c = [Distinct(Q)]

diag_c = []
for i in range(8):
    for j in range(i):
        if i == j:
            diag_c.append(True)
        else:
            diag_c.append(And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i))

solve(val_c + col_c + diag_c)
