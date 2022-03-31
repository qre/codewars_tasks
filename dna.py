#def DNA_strand(dna):
    #return dna.translate(string.maketrans("ATCG","TAGC")) #??

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])

def DNA_strand(dna):
    # code here
    dnaComplement=""
    for string in dna:
        if string=="A":
            dnaComplement+="T"
        elif string =="T":
            dnaComplement+="A"
        elif string =="G":
            dnaComplement+="C"
        elif string == "C":
            dnaComplement+="G"
    return dnaComplement

def DNA_strand(dna):
  return "".join([{'A':'T', 'T':'A', 'C':'G', 'G':'C'}[l] for l in dna])
