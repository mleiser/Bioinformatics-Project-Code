text = "TATAAGAAATTTCTGTTATATTCCGTAAAATCATAACAGACCACAGACCGGGTCTGGCTGCTCTCTCCAGTGAAGGGAGGGCAAGTTTACCCTGAGCTCAGGTACACAGATTGCGCCAGCACGCGGAAATCCTAGACGTTATTATACCACCCGCGATAACGTTAGAGTTCTAGATTATCCGTGTCATGAGCCCTGTAAGCATAGGCGCGACTGTATGAATATCAGGAACCTGCCCATGTAACGACAGCTATTTTTAAACAACATGCCCTTTAAGAGCGAAGGACGCGTGTGCATGAGCGACACTTATACTTTCTGACGCGTAAGGAAATTAAACAAATACTCC"
pattern = "AGGGAG"
d = 3

#Function to compute Hamming Distance
def HammingDistance(input1, input2):
    count = 0
    for i in range(0, len(input1)):
        if input1[i] != input2[i]:
            count = count + 1
    return count

#Computes the amount of k-mers within the specified Hamming Distance
def ApproximatePatternCount(text, pattern, d):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
	    compPattern = text[i : i + len(pattern)]
            if HammingDistance(pattern, compPattern) <= d:
                count = count + 1
    return count
print(ApproximatePatternCount(text, pattern, d))
