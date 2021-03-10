a = 220601
b = 190784
c = 100321
d = a - c
e = a - b
if d > e:
    print('d is greater')
else:
    print('e is greater')

X = False
Y = True
Z = (X and not Y) or (Y and not X)
print(Z)

W = X != Y
if W == Z:
    print(W == Z)
