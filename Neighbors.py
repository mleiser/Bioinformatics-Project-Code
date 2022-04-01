pattern = "AC"
d = 1

#Finds all k-mers within Hamming Distance 'd'            
def Neighbors(Pattern, d):

    #Sets up the exit conditions for the recursion
    if d == 0:
        return [Pattern]
    if len(Pattern) == 1:
        return ['A', 'C', 'G', 'T']
    Neighborhood = []

    #Finds the first letter of the sequence and saves the rest as the suffix pattern
    suffix = Pattern[1:]
    firstSymbol = Pattern[0]

    #Begins recursion to find all neighbors within d Hamming Distance
    SuffixNeighbors = Neighbors(suffix, d)
    for Text in SuffixNeighbors:

        #If the hamming distance is less than d, adds a nucleotide to the beginning and runs again
        if HammingDistance(suffix, Text) < d:
            for x in "AGCT":
                newText = x + Text
                if newText not in Neighborhood:
                    Neighborhood.append(newText)

        #Adds the first nucleotide from the original pattern to the text and adds to the neighborhood set
        else:
            newText = firstSymbol + Text
            if newText not in Neighborhood:
                Neighborhood.append(newText)
    return Neighborhood

#Finds the Hamming Distance between 2 patterns
def HammingDistance(input1, input2):
    count = 0
    #Finds the total mismatched nucleotides between the patterns
    for i in range(0, len(input1)):
        if input1[i] != input2[i]:
            count = count + 1
    return count

answer = Neighbors(pattern, d)
for i in answer:
    print(i)
