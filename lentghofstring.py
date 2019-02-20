## Another useful built-in tool in Pyhton is len function

#len("ATGC") BUT the len fuction does not put an outcome to the screen when we run
# the program. It only uoutputs a value that can be stored.


dna_length = len("AGCCCCTTGGAGATGACCCAGGTCCCCTTTTAATTATCCGGAAGAGAT")

print(dna_length)


dna_length = len("AGCCCCTTGGAGATGACCCAGGTCCCCTTTTAATTATCCGGAAGAGAT")
b = len("AAAAAAA")
print(str(b) + str(dna_length))



# if you run this code the result will be 48
#PYTHON TREATS STRINGS AND NUMBERS (INT // INTEGER) DIFFERENTLY

#BUT PYTHON HAS A SOLUTION FOR THAT. THE SOLUTION IS TO CREATE A STRING FOR
# THE NUMBER SO THAT WE CAN STCIK TO STRINGS TOGETHER

my_dna = "ATGCGAGT"
dna_length = len (my_dna)
print ("The length of the DNA sequence is" + " " + str(dna_length))
print(str(dna_length))
