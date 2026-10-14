def gc(dna):
    "This function computes the gc percentage of a dna sequence"
    nbases = dna.count('n') + dna.count('N')
    gcpercent = float(dna.count('c') + dna.count('C') + dna.count('g') + dna.count('G')) * 100 / (len(dna) - nbases)
    return gcpercent

def at(dna):
    "This function computes the at percentage of a dna sequence"
    nbases = dna.count('n') + dna.count('N')
    atpercent = float(dna.count('a') + dna.count('A') + dna.count('t') + dna.count('T')) * 100 / (len(dna) - nbases)
    return atpercent