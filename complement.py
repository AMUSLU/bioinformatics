##Complementing DNA

## Here is a short DNA sequence
#    ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT
# Write a program that will print the complement of this sequence

# Answer: this one seems straighforward! we need to take our sequence and replace
# A with T, T with A, C with G and G with C.

my_dna =  "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replacement1 = my_dna.replace('A', 't')
print(replacement1)
replacement2 = replacement1.replace('T', 'a')
print(replacement2)
replacement3 = replacement2.replace('C', 'g')
print(replacement3)
replacement4 = replacement3.replace('G', 'c')
print(replacement4)
print(replacement4.upper())

# result will be
# tCTGtTCGtTTtCGTtTtGTtTTTGCTtTCtTtCtTtTtTtTCGtTGCGTTCtT
# tCaGtaCGtaatCGatatGataaaGCataCtatCtatatataCGtaGCGaaCta
# tgaGtagGtaatgGatatGataaaGgatagtatgtatatatagGtaGgGaagta
# tgactagctaatgcatatcataaacgatagtatgtatatatagctacgcaagta
# TGACTAGCTAATGCATATCATAAACGATAGTATGTATATATAGCTACGCAAGTA

## THE OTHER WAY TO DO IT IS MUCH COMPLEX BUT JUST TO KNOW!!


my_dna =  "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
replacement1 = my_dna.replace('A', 'H')
print(replacement1)
replacement2 = replacement1.replace('T', 'J')
print(replacement2)
replacement3 = replacement2.replace('C', 'K')
print(replacement3)
replacement4 = replacement3.replace('G', 'L')
print(replacement4)
replacement5 = replacement4.replace('H', 'T')
print(replacement1)
replacement6 = replacement5.replace('J', 'A')
print(replacement2)
replacement7 = replacement6.replace('K', 'G')
print(replacement3)
replacement8 = replacement7.replace('L', 'C')

print(replacement8)

##RESULT
# HCTGHTCGHTTHCGTHTHGTHTTTGCTHTCHTHCHTHTHTHTCGHTGCGTTCHT
# HCJGHJCGHJJHCGJHJHGJHJJJGCJHJCHJHCHJHJHJHJCGHJGCGJJCHJ
# HKJGHJKGHJJHKGJHJHGJHJJJGKJHJKHJHKHJHJHJHJKGHJGKGJJKHJ
# HKJLHJKLHJJHKLJHJHLJHJJJLKJHJKHJHKHJHJHJHJKLHJLKLJJKHJ
# HCTGHTCGHTTHCGTHTHGTHTTTGCTHTCHTHCHTHTHTHTCGHTGCGTTCHT
# HCJGHJCGHJJHCGJHJHGJHJJJGCJHJCHJHCHJHJHJHJCGHJGCGJJCHJ
# HKJGHJKGHJJHKGJHJHGJHJJJGKJHJKHJHKHJHJHJHJKGHJGKGJJKHJ
# TGACTAGCTAATGCATATCATAAACGATAGTATGTATATATAGCTACGCAAGTA
