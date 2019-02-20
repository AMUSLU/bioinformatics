##restriction fragment length of DNA

## Here is a short DNA sequence
#    ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT
# This sequence contains a recognition site for the EcoRI restriction enzyme,
#which cuts at the motif G*AATTC
# Write a program which will calculate the size of the two fragments that will be
# produced when the DNA sequence is digested with EcoRI

my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
frag1_length = my_dna.find("GAATTC") + 1
frag2_length = len(my_dna) - frag1_length
print("length of fragment one is" + " " + str(frag1_length))
print("length of fragment two is" + " " + str(frag2_length))
