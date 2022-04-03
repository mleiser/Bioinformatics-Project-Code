genome = "GAGCCACCGCGATA"
def GeneSkew(genome):
    skew = [0]
    currentSkew = 0
    
    #Runs through the genome snip and adds the current skew to the list
    for i in range(0, len(genome)):
        
        #Substracts 1 from the current skew if 'C' nucleotide
        if genome[i] == "C":
            currentSkew = currentSkew - 1
            skew.append(currentSkew)
            
        #Adds 1 to the current skew if 'G' nucleotide
        elif genome[i] == "G":
            currentSkew = currentSkew + 1
            skew.append(currentSkew)
            
        #Adds current skew to list if 'A' or 'T' nucleotide    
        else:
            skew.append(currentSkew)
    return skew

output = GeneSkew(genome)
print(' '.join(map(str, output)))

