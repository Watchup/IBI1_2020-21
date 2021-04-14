def calculator(seq):
    '''
    input
        seq = the DNA sequence
    return
        reverse complement of a DNA strand
    '''
    seq = seq.upper()      # Upper () will change all lowercase to upper case so that subsequent operations only need to be uppercase
    seq_l = list(seq)
    seq_l.reverse()
    seq_s = "".join(seq_l)   # Lines 3 to 5 are used to reverse the DNA sequence

    R_C_DNA = []
    for i in seq_s:
        if i == 'A':                  # Lines 7 to 16 are used to obtain complementary chains.
            R_C_DNA.append('T')
        elif i == 'T':
            R_C_DNA.append('A')
        elif i == 'G':
            R_C_DNA.append('C')
        elif i == 'C':
            R_C_DNA.append('G')

    result = "".join(R_C_DNA)
    print(result)
    return result

# Example
calculator('ATATCTGCAGtagctagCAGtCTAg')
