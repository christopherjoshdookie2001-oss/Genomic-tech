def complement(dna):
    """Return the complement of the dna string."""
    basecomplement = {'A':'T','C':'G','G':'C','T':'A','N':'N','a':'t','c':'g','g':'c','t':'a','n':'n'}
    letters = list(dna)
    letters = [basecomplement[base] for base in letters]
    return ''.join(letters)

def reversecomplement(seq):
    """Return the reverse complement of the dna string."""
    seq = seq[::-1]
    seq = complement(seq)
    return seq