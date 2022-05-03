Dna = 'GATTGTAGCTTTCGTAACTATTATCAATATGACGGAACCGGG CAATATCTCCGGGAGTGTGACTTCAAGTGACATGATGGACGA ACAAATTTCGTCCAATACGGCAGACTGTGGGAAGCTCGGCGT ACAACCCAATAAGGAGAGTCGATTTCTCACTCTTACTAAGTT CAATATACCCGGCTCCGGCTGGGTGCACCGCTAAACTGAAGC CCATAACCATATACAATAATAGATAGTTGCCAATATAAGGAG CACGTAGTAGAGCAATATGTTTTTCGGCAACACAAGCCATCG TCATCACACTTGAATTACACCCGAATTAGCCAATATGCGCAT ATCGACACCATGATCATAATCAGTTGCAGATATTGTCAATAT TCAGTAGCTCGACGGCTAGATTTTCAATAGAAGCTAATTCTC'
k = 6

#Finds the amount of difference between 2 patterns
def HammingDistance(input1, input2):
    count = 0

    #Finds the total mismatched nucleotides between the patterns
    for i in range(len(input1)):
        if input1[i] != input2[i]:
            count = count + 1
    return count

#Finds the k-mer that minimizes d 
def MedianString(Dna, k):
    strings = []
    kmers = []
    strings = strings + Dna.split(' ')
    
    #Searches for the k-mer that minimizes d
    for sets in strings:
        stringDna = sets

        #Adds a list of specified length k-mers
        for i in range(len(stringDna) - k+1):
            pattern = stringDna[i:i + k]
            if pattern not in kmers:
                kmers.append(pattern)
        distance = 1000

        #Finds the k-mer that minimizes d in the list 
        for kmer in kmers:
            for i in range(len(stringDna) - k+1):
                if distance > HammingDistance(kmer, stringDna[i:i + k]):
                    distance = HammingDistance(kmer, stringDna[i:i + k])
                    median = kmer

    #returns the median k-mer
    return median

print(MedianString(Dna, k))
