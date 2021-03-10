# A total of 12 calculations were made
#Select the LOOP statement according to the transport rule
# Let's say that these three numbers are a,b and c
a = 1
b = 1
print(a)
print(b)
for i in range(1,12):
    c = a + b # Where c is equal to a plus b
    a = b    # And when calculations are done, the original c becomes the new b,
    b = c      # and the original b becomes the new c
    print(c)
