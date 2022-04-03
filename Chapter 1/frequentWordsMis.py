text = "CCCCATCAGGCCCCCCCCAGGAGGATCAGGAGGCCCCATCAGGAGGATCAGGCCCCAGGAGGACTAGGAGGATCCCCCAGGAGGAGGCCCCCCCCATCATCACTCCCCATCACTAGGAGGAGGATCCCCCCCCCAGGAGGCCCCAGGACTAGGACTACTCCCCAGGACTACTAGGACTATCATCATCAGGACTCCCCCCCCCCCCAGGAGGAGGATCAGGATCAGGATCAGGAGGCCCCATCAGGCCCCAGGAGGAGGACTATCCCCCCCCCAGGCCCCATCAGGACTAGGAGGAGGAGGCCCCAGGCCCCAGGAGGAGGCCCCATCAGGCCCCAGGACTATCAGGCCCCCCCCATCAGGCCCCATCAGGCCCCAGGAGGACTACTAGG"
k = 6
d = 2

#Returns a list of frequent k-mers with 'd' allowed mismatches
def FrequentWordsMis(text, k, d):
    patterns = []
    freqMap = {}
    n = len(text)

    #Generates the frequency map based on neighbor k-mers
    for i in range(0, n - k):
        pattern = text[i : i + k]

        #Returns a list of neighbors with less than 'd' mismatches
        neighborhood = Neighbors(pattern, d)
        for j in range(0, len(neighborhood) - 1):
            neighbor = neighborhood[j]

            #Counts the frequency of neighbor k-mers
            if neighbor not in freqMap:
                freqMap[neighbor] = 1
            else:
                freqMap[neighbor] = freqMap[neighbor] + 1
    return freqMap

            
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

freqMap = FrequentWordsMis(text, k, d)

#Finds the maximum value
maxValue = max(freqMap.items(), key = lambda x: x[1])

#Prints all keys with the maximum value
for key, value in freqMap.items():
    if value == maxValue[1]:
        print(key)
