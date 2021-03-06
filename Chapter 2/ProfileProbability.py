dna = "GACAAAACTGAAGTAGCTGAATAATTAGATCATTAAGATTCCTTATTACAGTAAGCCATCATTAACCCATGGCGGACACCCAGCGTACAGCGCAGTCGATTACGGGGTCCATTTCCATATCGAGAGCTCAACCGGTGGCACCATACCACCATTGAACGTATATAGATACGTACGAGACCGGTTGGTTGGTACGGTGGTTCTTGTCTTGGTCCTACGCTATGCTGGACTATGAGACAAAGTCTAACTTGCGGAAACGCGTTGCCTATTTTAGTGCATAGAAAGTACTGGGTTTCCCTGACGGCCGAAGACGCTCAATCATGCCACTTGTTATCCAAGGGCTTGACGCCAAAGCCCCTAGAGCAACTGCTCCCAGCTGACTAGCTTTCGGGAGTTCGGACTAATGAGGATATGAGTGCACCCAGAAGGTTCACGGCCGCACTGCACCGCCTCTAGGCGCTCTAAGGTTGTTGAAGATCAGAGTAAATGAGCACAGCTACTGCTCTACGAACTCACTCAATTTCCAAGACAAGTTTTTAATCGTTGAAGGTGGGGCGTTTTACCCCCTGAAATAGAGGCCATGAGTGAAGTCGGATCTACGGCTTTTCTCGGTCGCCGGCTCCATCCGCATCCTCATGGCGAGGGTCTGGCAACGAAAACGATCCTCCATCGGTAAGAAGACAGCCTAGGATGGGGGCTGAAAGCCAGTAGATTGACCTTCTCGCTTCCTTCCCAATCCTATTGACTAAAGTGACTTGTTATCAGCTAATCACTAACCTCTTTTCTGTCCTAGACCCCTGTTTGAAGTGGGAAATATCGACTAATTTAAACCGGTAGGGAATGCTAGCCTGCGATGTGAAGAATTCGATCTCTGGTGGAGCACCGTATAGGGACGAGCGTAGCTTGGCCGAGTTCGCATAAATCAGCCTGCGGTGTAGTGCCCACAGCTACGGAAATACGACACAAGGAGCGACGAATTGCTTGAAGCTCTTACAAAAGAAGT"

#Creates the probability matrix
profile = {
    'A': [0.313, 0.205, 0.253, 0.337, 0.265, 0.313, 0.169, 0.193, 0.253, 0.217, 0.193, 0.181],
    'C': [0.169, 0.193, 0.217, 0.217, 0.241, 0.157, 0.265, 0.313, 0.145, 0.205, 0.217, 0.337],
    'G': [0.241, 0.289, 0.361, 0.217, 0.205, 0.277, 0.277, 0.289, 0.325, 0.205, 0.386, 0.265],
    'T': [0.277, 0.313, 0.169, 0.229, 0.289, 0.253, 0.289, 0.205, 0.277, 0.373, 0.205, 0.217]
}

k = 12

#Finds the k-mer that has the highest probability based on the above matrix
def ProfileProbability(profile, k, dna):
    mostProbable = ""
    kmers = []
    currentMaxProb = 0

    #Creates a list of kmers of length k
    for i in range(len(dna) - k+1):
        if dna[i: i + k] not in kmers:
            kmers.append(dna[i: i + k])

    #Takes the kmers and multiplies the probabilites to find the highest        
    for strings in kmers:
        currentProb = 1
        for j in range(len(strings)):
            key = strings[j]
            probValue = profile[key][j]
            currentProb = currentProb * probValue

        #Tests if the newest kmer probability greater than the previous probability 
        if currentProb > currentMaxProb:
            currentMaxProb = currentProb
            mostProbable = strings
    return mostProbable

print(ProfileProbability(profile, k, dna))
