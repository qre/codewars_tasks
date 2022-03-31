def DNAtoRNA(dna):
    return "".join(["U" if c=="T" else c for c in dna])

def DNAtoRNA(dna):
    return dna.replace('T', 'U')