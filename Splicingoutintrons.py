# Here's a short section of genomic DNA:
# ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGAT
# CGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
# It comprises two exons and an intron. The first exon rubs from the start of
# the sequence to the sixty-third character to the end of the sequence.
# Write a program that will print just the coding regions of the DNA sequence.
my_dna = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'

exon1 = my_dna[0:62]
exon2 = my_dna[90:10000]
print(exon1 + exon2)



#Section 2 : Write a program that will calculate what percentage of the DNA
# squence is coding

my_dna = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'

exon1 = my_dna[0:62]
exon2 = my_dna[90:10000]
print(exon1 + exon2)
coding_length = len(exon1 + exon2)
total_length = len(my_dna)
print(100 * coding_length / total_length)

# Section 3:  Write a program that will print out the original genomic DNA
# sequence with coding bases in uppercases and non-coding bases in lowercases.

my_dna = 'ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT'

exon1 = my_dna[0:62]
intron = my_dna[62:90]
exon2 = my_dna[90:10000]
print(exon1 + intron.lower() + exon2)
print(my_dna[0:62] + my_dna[62:90].lower() + my_dna[90:10000])
