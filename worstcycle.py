"""Find the worst-quality sequencing cycle in any FASTQ file.

Usage (at the C:\\Users\\cjd20> prompt, not at >>>):
    python worstcycle.py path\\to\\reads.fastq
    python worstcycle.py path\\to\\reads.fastq 5      (show the 5 worst cycles)

Or from Python:
    from worstcycle import readFastq, cycle_stats
"""
import sys


def readFastq(filename):
    """Read a FASTQ file and return two lists: the bases and the quality strings."""
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()                  # line 1: read name (skip)
            seq = fh.readline().rstrip()   # line 2: bases
            fh.readline()                  # line 3: + (skip)
            qual = fh.readline().rstrip()  # line 4: quality scores
            if len(seq) == 0:              # nothing left, so stop
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities


def phred33ToQ(qual):
    """Turn one quality character into its score (Phred+33, used by modern Illumina files)."""
    return ord(qual) - 33


def cycle_stats(seqs, quals):
    """For each position, return (average quality, number of N's, number of reads that reach it)."""
    read_len = max(len(q) for q in quals)
    total_q = [0] * read_len   # sum of quality scores at each position
    n_count = [0] * read_len   # how many reads have an N at each position
    covered = [0] * read_len   # how many reads are long enough to reach each position

    for seq, qual in zip(seqs, quals):
        for i in range(len(qual)):
            total_q[i] += phred33ToQ(qual[i])
            covered[i] += 1
            if seq[i] in 'Nn':
                n_count[i] += 1

    stats = []
    for i in range(read_len):
        avg = total_q[i] / covered[i] if covered[i] else 0
        stats.append((avg, n_count[i], covered[i]))
    return stats


def main():
    if len(sys.argv) < 2:
        print("Usage: python worstcycle.py <file.fastq> [how_many_worst]")
        sys.exit(1)

    filename = sys.argv[1]
    how_many = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    seqs, quals = readFastq(filename)
    if not seqs:
        print("No reads found in", filename)
        sys.exit(1)

    stats = cycle_stats(seqs, quals)
    overall = sum(s[0] * s[2] for s in stats) / sum(s[2] for s in stats)

    print("File:", filename)
    print("Number of reads:", len(seqs))
    print("Longest read:", len(stats), "bases")
    print("Overall average quality:", round(overall, 2))
    print()

    # Sort positions from worst average quality to best
    order = sorted(range(len(stats)), key=lambda i: stats[i][0])
    print("Worst cycle(s), 0-based:")
    for i in order[:how_many]:
        avg, ns, cov = stats[i]
        print(f"  cycle {i}: average quality {avg:.2f}, N in {ns} of {cov} reads")


if __name__ == "__main__":
    main()