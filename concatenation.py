# we can combine two string in one variable by using "+" symbol between two strings

my_dna = "AATT" + "GGCC"
print(my_dna)


# we can also stick together the variables that points to strings:

upstream = "AAA"
my_dna = upstream + "ATTC"
print(my_dna)


a = "red"
b = a + "c"
c = "red"
print(b+c)


upstream="AAA"
downstream="GGG"
my_dna=upstream + "ATGC" + downstream
print(my_dna)


## so it is totally fine to combine two string in one variable as well.
print("hello" + "World")
