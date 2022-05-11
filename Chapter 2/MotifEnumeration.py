Dna = ["AGGGACTCGCGCCTCCCTGTAAAGG", "AGCTCAATGTGTTCCCCACTGGATG", "CCTCTGAACAGATGTGAACCTTGCG", "TCTGATCCACGCCATCTTTTCCAAT", "CAGACGATCACCAATGTTTCAAGAG", "AGCAGAGCCCCCGTTTCTTACAGGG"]
k = 5
d = 2
#Finds all k-mers within Hamming Distance 'd'            

def Neighbors(Pattern, d):

    #Sets up the exit conditions for the recursion
    if d == 0:
        return {Pattern}
    elif len(Pattern) == 1:
        return ['A', 'C', 'G', 'T']
    Neighborhood = set()

    #Finds the first letter of the sequence and saves the rest as the suffix pattern
    suffix = Pattern[1:]
    firstSymbol = Pattern[0]

    #Begins recursion to find all neighbors within d Hamming Distance
    SuffixNeighbors = Neighbors(suffix, d)
    for Text in SuffixNeighbors:

        #If the hamming distance is less than d, adds a nucleotide to the beginning and runs again
        if HammingDistance(suffix, Text) < d:
            for x in "ATCG":
                newText = x + Text
                Neighborhood.add(newText)

        #Adds the first nucleotide from the original pattern to the text and adds to the neighborhood set
        else:
            baseText = firstSymbol + Text
            Neighborhood.add(baseText)
    return Neighborhood   

#Finds the Hamming Distance between 2 patterns
def HammingDistance(input1, input2):
    count = 0

    #Finds the total mismatched nucleotides between the patterns
    for i in range(len(input1)):
        if input1[i] != input2[i]:
            count = count + 1
    return count

#Finds the most common kmer patterns of mismatch limit d
def MotifEnumeration(Dna, k, d):
    kmers = [set() for _ in Dna]
    
    #Finds all possible kmer patterns
    for pos, pattern in enumerate(Dna):
        for i in range(len(pattern) - k + 1):
            neighborhood = Neighbors(pattern[i: i + k], d)
            kmers[pos].update(neighborhood)
    patterns = kmers[0]
    #Combines the sets and patterns into 1 list
    for sets in kmers:
        patterns = patterns & sets
    
    #Returns the most frequent patterns
    return patterns

output = MotifEnumeration(Dna, k, d)
print(' '.join(output))
