def proteins(strand):
    list_of_proteins = []
    prot_dict = {
        'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
        'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine',
        'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
        'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UGU': 'Cysteine',
        'UGC': 'Cysteine', 'UGG': 'Tryptophan', 'UAA': 'STOP',
        'UAG': 'STOP', 'UGA': 'STOP'
    }

    list_of_codons = [strand[i: i+3] for i in range(0, len(strand), 3)]
    list_of_proteins = [prot_dict[cod] for cod in list_of_codons]

    if 'STOP' in list_of_proteins:
        stop_position = list_of_proteins.index('STOP')
        return list_of_proteins[:stop_position]
    return list_of_proteins
