def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            if not line[0] == '>':
                genome += line.rstrip()
    return genome

def naive(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        if t[i:i+len(p)] == p:
            occurrences.append(i)
    return occurrences

def naive_with_rc(p, t):
    rc = reverseComplement(p)
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        window = t[i:i+len(p)]
        if window == p or window == rc:
            occurrences.append(i)
    return occurrences

def naive_2mm(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):
        mismatches = 0
        for j in range(len(p)):
            if t[i+j] != p[j]:
                mismatches += 1
                if mismatches > 2:
                    break
        if mismatches <= 2:
            occurrences.append(i)
    return occurrences