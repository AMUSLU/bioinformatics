#count takes a single argument whore type is string, and returns the number of
# times that the argument is found in the variable. we have to use "str"
# to turn the counts into strings so that we can print them!!

protein = "vlspadktnv"

#count amino acid residues

valine_count = protein.count('v')
lsp_count = protein.count('lsp')
tryptophan_count = protein.count('w')


#now print the count
print("valines:" + str(valine_count))
print("lsp:" + str(lsp_count))
print("tryptophan:" + str(tryptophan_count))

## NOW FINDING METHOD: THIS METHOD HELPS US TO FIND ANY PROTEIN ON GIVING PRT CODE

protein = "vlspadktnv"
print (str(protein.find ('p')))
print (str(protein.find ('kt')))
print (str(protein.find ('w')))
 ### counting start at ZERO ###
 # RESULT 3 , 6 AND -1 (BECAUSE "W" DOES NOT EXIST)

 
