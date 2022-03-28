genome = "GAGCCACCGCGATA"
def geneSkew(genome):
    skew = [0]
    currentSkew = 0
    for i in range(0, len(genome)):
        if genome[i] == "C":
            currentSkew = currentSkew - 1
            skew.append(currentSkew)
        elif genome[i] == "G":
            currentSkew = currentSkew + 1
            skew.append(currentSkew)
        else:
            skew.append(currentSkew)
    return skew

output = geneSkew(genome)
print(' '.join(map(str, output)))

