import os
from blosum_dictionary import blosum62
# To make this page cleaner, I put the Blosum62 matrix in another file and then imported it

# Read the sequence
mouse = open('SOD2_mouse.fa')
human = open('SOD2_human.fa')
random = open('RandomSeq.fa')
lines_mouse = mouse.readlines()
lines_human = human.readlines()
lines_random = random.readlines()


def compare(seq1, seq2):
    score = 0
    distance = 0
    for	i in range(len(seq1)):
        if	seq1[i]!=seq2[i]:
            distance +=	1   # Count the number of different terms

        if (seq1[i], seq2[i]) in blosum62:
            score = score + blosum62[seq1[i], seq2[i]]
        else:
            score = score + blosum62[seq2[i], seq1[i]]

    percentage = 1- distance/len(seq1)
    print('The alignment score is ' + str(score))
    print('the percentage of identical amino acids is ' + str(percentage))

print(lines_human)
print(lines_mouse)
compare(lines_human[1][:-1], lines_mouse[1][:-1])

print(lines_human)
print(lines_random)
compare(lines_human[1][:-1], lines_random[1][:-1])

print(lines_mouse)
print(lines_random)
compare(lines_mouse[1][:-1], lines_random[1][:-1])
