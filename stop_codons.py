def stop_codon(dna, frame=0):
    "This function checks if given dna sequence has in frame stop codons."
    stop_codon_found = False
    stop_codons = ['tga', 'tag', 'taa']
    for i in range(frame, len(dna), 3):
        codon = dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found = True
            print("Stop codon", codon, "found at position", i + 1)
            break
    if not stop_codon_found:
        print("No in-frame stop codon found")
    return stop_codon_found