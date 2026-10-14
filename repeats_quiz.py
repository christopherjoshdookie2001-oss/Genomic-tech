from Bio import SeqIO
from collections import Counter

def find_orfs(seq, frame):
    """Return a list of (start_position, length) for every ORF in the given frame (1, 2 or 3)."""
    seq = str(seq).upper()
    stops = {"TAA", "TAG", "TGA"}
    orfs = []
    start = None
    for i in range(frame - 1, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if start is None and codon == "ATG":
            start = i
        elif start is not None and codon in stops:
            orfs.append((start + 1, i + 3 - start))
            start = None
    return orfs

def count_repeats(records, k):
    """Count every substring of length k across all sequences, including overlaps."""
    counts = Counter()
    for r in records:
        s = str(r.seq).upper()
        for i in range(len(s) - k + 1):
            counts[s[i:i+k]] += 1
    return counts

records = list(SeqIO.parse(r"C:\Users\cjd20\Downloads\dna2.fasta", "fasta"))

# Question 7: longest ORF in one specific sequence, any forward frame
target = "gi|142022655|gb|EQ086233.1|16"
for r in records:
    if r.id == target:
        longest = max(length for frame in (1, 2, 3) for start, length in find_orfs(r.seq, frame))
        print("Q7 - longest ORF in", target, ":", longest)

# Question 8: most frequent repeat of length 6
counts6 = count_repeats(records, 6)
repeat, times = counts6.most_common(1)[0]
print("Q8 - most frequent 6-base repeat:", repeat, "occurs", times, "times")

# Question 9: how many different 12-base repeats occur the maximum number of times
counts12 = count_repeats(records, 12)
max_count = max(counts12.values())
tied = [rep for rep, c in counts12.items() if c == max_count]
print("Q9 - Max =", max_count, "and", len(tied), "different 12-base sequences occur that many times:", tied)
# Question 10: which of these 7-base repeats occurs the maximum number of times
counts7 = count_repeats(records, 7)
max7 = max(counts7.values())
print("Q10 - Max for length 7 =", max7)
for rep in ["CATCGCC", "AATGGCA", "CGCGCCG", "TGCGCGC"]:
    print("  ", rep, counts7[rep])