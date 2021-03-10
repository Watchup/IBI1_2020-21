r = 1.2
#•means that each infected individual will on average infect 1.2 individuals.
n = 84     #The initial number
x = 5      # rounds
i = 0
while i < 5:
    n = n + n * r
    i = i + 1
# After five rounds it should be the number of r to the fifth power
print('''The r rate is''' + str(r))
print('''and the total number of individuals is ''' + str(n))
#input('How many individuals will each infected individual on average infect?')
