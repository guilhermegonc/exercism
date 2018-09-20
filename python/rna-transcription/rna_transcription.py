def to_rna(dna='acgt'):
    rna = ''
    for char in dna:
        if char in 'Gg':
            rna += 'C'
        elif char in 'Cc':
            rna += 'G'
        elif char in 'Tt':
            rna += 'A'
        elif char in 'Aa':
            rna += 'U'
        else:
            rna = 'RNA not valid'
            break
    return rna
