import re, os
from DNA_to_protein import translate  #To simplify the code, introduce functions from the Python files you wrote earlier as modules

file = open(input())
lines = file.readlines()     # get the data from the file

result = []
for i in range(0, len(lines)):
    if lines[i].startswith(">"):  # Find the description
        if 'unknown function' in lines[i]:  # Check whether it is unknown function
            result.append(re.findall(r'(>.+?)(?:_| )', lines[i])[0])
            bases = ''
            for n in range(0, len(lines[i:-1])):
                if not lines[i+n+1].startswith(">"):  # Skip the description line
                    bases += lines[i+n+1][:-1]
                    protein_sequence = translate(bases)   #Translate the DNA into a protein sequence using the translate function
                else:
                    break
            protein_sequence += "\n"
            result.append(protein_sequence)

for i in range(0, len(result)):   # Read the length of the protein
    if result[i].startswith(">"):
        result[i] += "  "
        result[i] += str(len(result[i+1]) - 1)
        result[i] += "\n"

with open('unknown_protein.fa','w') as output:
    unknown_function = open('unknown_protein.fa', "w")
for line in result:     #To branch out, the names and sequences of different protein are separated using a for loop
    unknown_function.write(line)
unknown_function.close()
