import numpy as np
import matplotlib.pyplot as plt    # import two modules

gene_lengths=[9410,394141,4442,105338,19149,76779,126550,36296,842,15981]
exon_counts=[51,1142,42,216,25,650,32533,57,1,523]
zipped = zip(gene_lengths, exon_counts)
zipped_list = list(zipped)
print(zipped_list)         #It can match gene_lengths and exon_counts one to one

gene_lengths_array = np.array(gene_lengths)
exon_counts_array = np.array(exon_counts)
exon_lenght = gene_lengths_array/exon_counts_array
                                    # exon_lenght = gene_lengths / exon_counts
                                    # Lists cannot be numerically evaluated;
                                    # they must be converted to Arrays
fig1, ax1 = plt.subplots()
ax1.boxplot(exon_lenght,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False,
              )   # Some basic properties of boxplot
ax1.set(title = 'exon lenght',)

plt.show()
