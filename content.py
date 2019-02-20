## Calculating AT Content in short DNA Sequence

#Example: ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT

#WRITE A PRGRAM THAT WILL PRINT OUT THE AT CONTENT OF THIS DNA AEQUENCE

#Answer
# AT CONTENT = A+T/LENGTH

my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')

print("length:" + str(length))
print("A:" + str(a_count))
print("T:" + str(t_count))

#this is look okay but how we know that we did correct coding? Let's check it!!
test_dna = "ATGC"

length = len(test_dna)
a_count = test_dna.count('A')
t_count = test_dna.count('T')

print("length:" + str(length))
print("A:" + str(a_count))
print("T:" + str(t_count))

#Seems working so let's contunie to calculate !!

length = len(test_dna)
a_count = test_dna.count('A')
t_count = test_dna.count('T')
at_content = (a_count + t_count) / length
print("AT content is" + " " +str(at_content))


#NOW WE CAN TRY ON OUR ORIGINAL QUESTIO
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
length = len(my_dna)
a_count = my_dna.count('A')
t_count = my_dna.count('T')
at_content = (a_count + t_count) / length
print("AT content is" + " " +str(at_content))
